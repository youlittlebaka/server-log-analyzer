from log_analyzer.parser import parse_logs


def test_parse_logs(tmp_path):
    log_file = tmp_path / "test.log"

    log_file.write_text(
        "2026-11-08 10:15:23 INFO Server started\n"
        "2026-11-08 10:16:10 ERROR Database failed\n"
    )

    logs = parse_logs(str(log_file))

    assert len(logs) == 2

    assert logs[0] == {
        "date": "2026-11-08",
        "time": "10:15:23",
        "level": "INFO",
        "message": "Server started"
    }

    assert logs[1]["level"] == "ERROR"