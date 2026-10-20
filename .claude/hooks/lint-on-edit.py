#!/usr/bin/env python3
"""PostToolUse hook: format and lint a Python file right after Claude edits it.

Reads the hook input JSON from stdin, takes tool_input.file_path, and runs
`ruff format` then `ruff check --fix` on it. If lint errors remain, exits
with code 2 so the messages are fed back to Claude (the edit has already
happened; this tells Claude what to fix). Skips silently when ruff is not
installed or the file is not Python.
Docs: https://code.claude.com/docs/en/hooks
"""

import json
import shutil
import subprocess
import sys


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0

    file_path = (payload.get("tool_input") or {}).get("file_path", "")
    if not file_path.endswith(".py"):
        return 0

    ruff = shutil.which("ruff")
    if ruff is None:
        return 0

    subprocess.run([ruff, "format", "--quiet", file_path], check=False)
    result = subprocess.run(
        [ruff, "check", "--fix", "--quiet", file_path],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        output = (result.stdout + result.stderr).strip()
        print(f"ruff found issues in {file_path}:\n{output}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
