from log_analyzer.analyzer import analyze_logs


def test_analyze_logs():
    logs = [
        {
            "date": "2026-11-08",
            "time": "10:15:23",
            "level": "INFO",
            "message": "Server started"
        },
        {
            "date": "2026-11-08",
            "time": "10:16:10",
            "level": "ERROR",
            "message": "Database failed"
        },
        {
            "date": "2026-11-08",
            "time": "10:17:45",
            "level": "ERROR",
            "message": "Database failed"
        }
    ]

    report = analyze_logs(logs, "2026-11-08")

    assert report["total_logs"] == 3
    assert report["level_count"]["INFO"] == 1
    assert report["level_count"]["ERROR"] == 2
    assert report["most_common_error"] == "Database failed"
    assert report["error_percentage"] == 66.67
    assert report["date_level_count"]["ERROR"] == 2