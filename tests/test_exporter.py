import json
import csv

from log_analyzer.exporter import export_json, export_csv


def test_export_json(tmp_path):
    report = {
        "total_logs": 2,
        "error_percentage": 50.0
    }

    output_file = tmp_path / "report.json"

    export_json(report, str(output_file))

    with open(output_file, "r") as file:
        saved_report = json.load(file)

    assert saved_report == report


def test_export_csv(tmp_path):
    logs = [
        {
            "date": "2026-11-08",
            "time": "10:15:23",
            "level": "INFO",
            "message": "Server started"
        }
    ]

    output_file = tmp_path / "logs.csv"

    export_csv(logs, str(output_file))

    with open(output_file, "r", newline="") as file:
        reader = csv.DictReader(file)
        saved_logs = list(reader)

    assert len(saved_logs) == 1
    assert saved_logs[0]["level"] == "INFO"
    assert saved_logs[0]["message"] == "Server started"