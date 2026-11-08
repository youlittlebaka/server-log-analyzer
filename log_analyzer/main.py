from parser import parse_logs
from analyzer import analyze_logs
from exporter import export_json, export_csv


LOG_FILE = "log_analyzer/logs/server.log"
JSON_FILE = "log_analyzer/reports/reports.json"
CSV_FILE = "log_analyzer/reports/logs.csv"

TARGET_DATE = "2026-11-08"


def main():
    # Parse logs
    logs = parse_logs(LOG_FILE)

    # Analyze logs
    report = analyze_logs(logs, TARGET_DATE)

    # Export reports
    export_json(report, JSON_FILE)
    export_csv(logs, CSV_FILE)

    print("Log analysis completed.")
    print(f"Total logs: {report['total_logs']}")
    print(f"Error percentage: {report['error_percentage']}%")
    print(f"Most common error: {report['most_common_error']}")
    print(f"JSON report: {JSON_FILE}")
    print(f"CSV report: {CSV_FILE}")


if __name__ == "__main__":
    main()