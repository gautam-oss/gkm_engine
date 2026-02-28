"""Tests for gkm_engine.core."""

from gkm_engine import run, __version__
from gkm_engine.core import _build_report


def test_version():
    assert __version__ == "0.1.0"


def test_run_executes(capsys):
    run()
    captured = capsys.readouterr()
    assert "gkm_engine" in captured.out
    assert "Engine started successfully" in captured.out


def test_build_report_contains_expected_fields():
    report = _build_report()
    assert "v0.1.0" in report
    assert "Python" in report
    assert "Platform" in report
    assert "Time" in report
    assert "UTC" in report