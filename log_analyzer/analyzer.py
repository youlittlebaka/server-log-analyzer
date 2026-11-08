def analyze_logs(logs, target_date):
    level_count = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0,
        "CRITICAL": 0
    }

    error_counts = {}

    # Count log levels and error messages
    for log in logs:
        level = log["level"]

        if level in level_count:
            level_count[level] += 1

        if level == "ERROR":
            error_message = log["message"]
            error_counts[error_message] = (
                error_counts.get(error_message, 0) + 1
            )

    # Find the most common error
    most_common_error = None

    if error_counts:
        most_common_error = max(
            error_counts.items(),
            key=lambda item: item[1]
        )[0]

    # Calculate error percentage
    total_logs = len(logs)
    total_errors = level_count["ERROR"]

    error_percentage = 0

    if total_logs > 0:
        error_percentage = round(
            total_errors / total_logs * 100, 2
        )

    # Filter logs by date
    filtered_logs = [
        log for log in logs
        if log["date"] == target_date
    ]

    # Count levels for the selected date
    date_level_count = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0,
        "CRITICAL": 0
    }

    for log in filtered_logs:
        if log["level"] in date_level_count:
            date_level_count[log["level"]] += 1

    # Build the report
    report = {
        "total_logs": total_logs,
        "level_count": level_count,
        "error_counts": error_counts,
        "most_common_error": most_common_error,
        "error_percentage": error_percentage,
        "date_level_count": date_level_count
    }

    return report