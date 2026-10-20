"""Flight metrics: pure functions over a list of samples."""

from collections.abc import Callable

from missionlog.telemetry import Sample


def duration(samples: list[Sample]) -> float:
    """Flight duration in seconds (last timestamp minus first)."""
    if len(samples) < 2:
        return 0.0
    return samples[-1].t - samples[0].t


def max_altitude(samples: list[Sample]) -> float:
    """Highest altitude reached, in metres above take-off."""
    return max((s.alt for s in samples), default=0.0)


def distance(samples: list[Sample]) -> float:
    """Ground distance in metres, integrating speed with the trapezoidal rule."""
    total = 0.0
    for a, b in zip(samples, samples[1:], strict=False):
        dt = b.t - a.t
        if dt <= 0:
            continue
        total += (a.speed + b.speed) / 2 * dt
    return total


def battery_used(samples: list[Sample]) -> float:
    """Battery consumed during the flight, in percentage points."""
    if len(samples) < 2:
        return 0.0
    return samples[0].battery - samples[-1].battery


METRICS: dict[str, tuple[str, Callable[[list[Sample]], float]]] = {
    "duration": ("Duration (s)", duration),
    "max_altitude": ("Max altitude (m)", max_altitude),
    "distance": ("Distance (m)", distance),
    "battery_used": ("Battery used (%)", battery_used),
}
