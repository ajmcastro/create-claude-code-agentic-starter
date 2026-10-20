"""Command-line entry point: print a flight summary."""

import argparse

from missionlog.metrics import METRICS
from missionlog.telemetry import load_samples


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Summarise a flight telemetry CSV.")
    parser.add_argument("csv", help="path to a telemetry CSV file")
    args = parser.parse_args(argv)

    samples = load_samples(args.csv)
    width = max(len(label) for label, _ in METRICS.values())
    print(f"Samples: {len(samples)}")
    for label, func in METRICS.values():
        print(f"{label:<{width}}  {func(samples):10.2f}")
    return 0
