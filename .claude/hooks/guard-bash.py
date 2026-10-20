#!/usr/bin/env python3
"""PreToolUse hook: block destructive shell commands before they run.

Claude Code passes the hook input as JSON on stdin; for the Bash tool the
command is at tool_input.command. Exiting with code 2 blocks the tool call
and the stderr message is shown to Claude so it can change course.
Docs: https://code.claude.com/docs/en/hooks
"""

import json
import re
import sys

BLOCKED = [
    (
        r"\bgit\s+push\b.*(--force\b|-f\b|--force-with-lease\b)",
        "force-push is not allowed in this repo",
    ),
    (r"\bgit\s+reset\s+--hard\b", "git reset --hard discards work; ask the user first"),
    (r"\brm\s+-[a-zA-Z]*r[a-zA-Z]*f?\s+(/|~|\$HOME)(\s|$)", "recursive delete of a root/home path"),
    (r"\brm\s+-[a-zA-Z]*r[a-zA-Z]*\s+.*\bdata/", "data/ is read-only reference input"),
    (r"(curl|wget)\b.*\|\s*(sh|bash)\b", "piping a download into a shell"),
]


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0  # Not our problem; never block on malformed input.

    command = (payload.get("tool_input") or {}).get("command", "")
    for pattern, reason in BLOCKED:
        if re.search(pattern, command):
            print(f"Blocked by guard-bash hook: {reason}. Command: {command}", file=sys.stderr)
            return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
