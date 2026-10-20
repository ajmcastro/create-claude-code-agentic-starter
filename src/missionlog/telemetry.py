"""Parse telemetry CSV files into Sample records."""

import csv
from dataclasses import dataclass
from pathlib import Path

REQUIRED_COLUMNS = ("t", "alt", "speed", "battery")


@dataclass(frozen=True)
class Sample:
    """One telemetry reading.

    t: seconds since recording start
    alt: metres above take-off point
    speed: ground speed in m/s
    battery: state of charge in percent
    """

    t: float
    alt: float
    speed: float
    battery: float


def load_samples(path: str | Path) -> list[Sample]:
    """Read a telemetry CSV and return samples sorted by time."""
    with open(path, newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        missing = [c for c in REQUIRED_COLUMNS if c not in (reader.fieldnames or [])]
        if missing:
            raise ValueError(f"missing columns: {', '.join(missing)}")
        samples = [
            Sample(
                t=float(row["t"]),
                alt=float(row["alt"]),
                speed=float(row["speed"]),
                battery=float(row["battery"]),
            )
            for row in reader
        ]
    return sorted(samples, key=lambda s: s.t)
