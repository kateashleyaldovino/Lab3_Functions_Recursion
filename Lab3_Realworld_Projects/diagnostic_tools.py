def validate_telemetry(value):
    try:
        value = float(value)

        if value < 0 or value > 60:
            return False

        return True

    except (ValueError, TypeError):
        return False


def monitor_process(func):
    def wrapper(*args, **kwargs):
        print("\n[LOG] Processing telemetry data started.")
        result = func(*args, **kwargs)
        print("[LOG] Processing telemetry data completed.")
        return result

    return wrapper


def recursive_analysis(value, trace=None):
    if trace is None:
        trace = []

    trace.append(value)

    if value <= 30:
        return trace

    return recursive_analysis(value - 10, trace)


@monitor_process
def process_telemetry(data):
    results = []

    for value in data:
        try:
            if not validate_telemetry(value):
                results.append((value, "INVALID"))
                continue

            transformed = lambda x: x * 1.0
            processed_value = transformed(value)

            if processed_value > 50:
                status = "CRITICAL"
            elif processed_value > 30:
                status = "ABNORMAL"
            else:
                status = "NORMAL"

            results.append((processed_value, status))

        except (ValueError, TypeError):
            results.append((value, "INVALID"))

    return results