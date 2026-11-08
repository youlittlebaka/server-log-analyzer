import csv
import json
from pathlib import Path


def export_json(report, file_path):
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, "w") as file:
        json.dump(report, file, indent=4)


def export_csv(logs, file_path):
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)

    fieldnames = ["date", "time", "level", "message"]

    with open(file_path, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(logs)