import pytest

from missionlog.telemetry import load_samples


def test_load_samples_sorts_by_time(tmp_path):
    path = tmp_path / "f.csv"
    path.write_text("t,alt,speed,battery\n2,1,1,90\n0,0,0,100\n1,1,1,95\n")
    samples = load_samples(path)
    assert [s.t for s in samples] == [0.0, 1.0, 2.0]


def test_load_samples_rejects_missing_columns(tmp_path):
    path = tmp_path / "f.csv"
    path.write_text("t,alt\n0,0\n")
    with pytest.raises(ValueError, match="speed"):
        load_samples(path)
