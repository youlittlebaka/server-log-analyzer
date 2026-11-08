def parse_logs(file_path):
    logs = []

    with open(file_path, "r") as file:
        for line in file:
            clean_line = line.strip()

            if not clean_line:
                continue

            parts = clean_line.split(maxsplit=3)

            if len(parts) != 4:
                continue

            date = parts[0]
            time = parts[1]
            level = parts[2]
            message = parts[3]

            log_entry = {
                "date": date,
                "time": time,
                "level": level,
                "message": message
            }

            logs.append(log_entry)

    return logs