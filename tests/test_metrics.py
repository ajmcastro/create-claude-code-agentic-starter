import pytest

from missionlog.metrics import METRICS, battery_used, distance, duration, max_altitude
from missionlog.telemetry import Sample


@pytest.fixture
def flight() -> list[Sample]:
    return [
        Sample(t=0.0, alt=0.0, speed=0.0, battery=100.0),
        Sample(t=10.0, alt=50.0, speed=10.0, battery=98.0),
        Sample(t=20.0, alt=80.0, speed=10.0, battery=96.0),
        Sample(t=30.0, alt=0.0, speed=0.0, battery=93.0),
    ]


def test_duration(flight):
    assert duration(flight) == 30.0


def test_max_altitude(flight):
    assert max_altitude(flight) == 80.0


def test_distance_trapezoidal(flight):
    # 0→10: avg 5 m/s * 10 s = 50; 10→20: 100; 20→30: 50
    assert distance(flight) == pytest.approx(200.0)


def test_distance_skips_zero_duration_intervals():
    samples = [
        Sample(t=0.0, alt=0.0, speed=10.0, battery=100.0),
        Sample(t=0.0, alt=0.0, speed=10.0, battery=100.0),
        Sample(t=1.0, alt=0.0, speed=10.0, battery=100.0),
    ]
    assert distance(samples) == pytest.approx(10.0)


def test_battery_used(flight):
    assert battery_used(flight) == 7.0


@pytest.mark.parametrize("_label, func", list(METRICS.values()))
def test_every_metric_handles_empty_input(_label, func):
    assert func([]) == 0.0
