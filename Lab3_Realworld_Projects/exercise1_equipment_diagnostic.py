LAST_NAME = "ALDOVINO"
SEED_NUM = 8
FAVORITE_ARTIST = "BINI"

equipment_data = [29, 47, 48, 16, 24]


def validate_reading(reading):
    try:
        reading = float(reading)

        if reading < 0:
            return False

        return True

    except (ValueError, TypeError):
        return False


def classify_reading(reading):
    if reading < 30:
        return "LOW"
    elif reading <= 50:
        return "NORMAL"
    else:
        return "HIGH"


def diagnostic_log(func):
    def wrapper(*args, **kwargs):
        print("\n[LOG] Diagnostic process started.")
        result = func(*args, **kwargs)
        print("[LOG] Diagnostic process completed.")
        return result

    return wrapper


@diagnostic_log
def process_readings(data):
    results = []

    for reading in data:
        if validate_reading(reading):
            condition = classify_reading(reading)
            results.append((reading, condition))
        else:
            results.append((reading, "INVALID"))

    return results


print("=== EQUIPMENT DIAGNOSTIC SYSTEM ===")
print("Engineer:", LAST_NAME)
print("Seed Number:", SEED_NUM)
print("Favorite Artist:", FAVORITE_ARTIST)

print("\nGenerated Equipment Data:")
print(equipment_data)

results = process_readings(equipment_data)

print("\nDiagnostic Results:")
for reading, condition in results:
    print(f"{reading} -> {condition}")


low_count = sum(1 for _, condition in results if condition == "LOW")
normal_count = sum(1 for _, condition in results if condition == "NORMAL")
high_count = sum(1 for _, condition in results if condition == "HIGH")

print("\nSummary:")
print("LOW:", low_count)
print("NORMAL:", normal_count)
print("HIGH:", high_count)