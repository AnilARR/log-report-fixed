import json
from pathlib import Path

REPORT = Path("/app/report.json")


def load_report():
    with REPORT.open() as f:
        return json.load(f)


def test_report_exists():
    """Success criterion 1: Report is written to /app/report.json."""
    assert REPORT.exists(), "report.json was not created"


def test_total_requests():
    """Success criterion 2: total_requests equals the number of log entries."""
    report = load_report()
    assert report["total_requests"] == 6


def test_unique_ips():
    """Success criterion 3: unique_ips equals the number of distinct client IPs."""
    report = load_report()
    assert report["unique_ips"] == 3


def test_top_path():
    """Success criterion 4: top_path is the most frequently requested URL path."""
    report = load_report()
    assert report["top_path"] == "/index.html"


def test_valid_json():
    """Success criterion 5: Output is valid JSON."""
    report = load_report()
    assert isinstance(report, dict)