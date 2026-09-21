from telemetry_generator import generate_telemetry
from diagnostic_tools import process_telemetry, recursive_analysis


LAST_NAME = "ALDOVINO"
SEED_NUM = 8
FAVORITE_ARTIST = "BINI"


print("=== INTELLIGENT EQUIPMENT MONITORING PIPELINE ===")

print("\nStudent-Specific Inputs:")
print("Engineer:", LAST_NAME)
print("Seed Number:", SEED_NUM)
print("Favorite Artist:", FAVORITE_ARTIST)


telemetry_stream = generate_telemetry(
    LAST_NAME,
    SEED_NUM,
    FAVORITE_ARTIST
)

telemetry_data = list(telemetry_stream)

print("\nGenerated Telemetry Data:")
print(telemetry_data)


# Add an invalid value to demonstrate exception handling
telemetry_data.append("INVALID")


print("\nTelemetry Data with Invalid Entry:")
print(telemetry_data)


processed_results = process_telemetry(telemetry_data)


print("\nProcessed Results:")

valid_count = 0
invalid_count = 0
abnormal_count = 0
critical_count = 0

for value, status in processed_results:
    print(f"{value} -> {status}")

    if status == "INVALID":
        invalid_count += 1

    else:
        valid_count += 1

        if status == "ABNORMAL":
            abnormal_count += 1

        elif status == "CRITICAL":
            critical_count += 1


print("\nRecursive Analysis:")

abnormal_values = [
    value
    for value, status in processed_results
    if status in ("ABNORMAL", "CRITICAL")
]


if abnormal_values:
    for value in abnormal_values:
        trace = recursive_analysis(value)
        print(f"{value} -> {trace}")
else:
    print("No abnormal conditions detected.")


processed_count = len(processed_results)


if critical_count > 0:
    overall_status = "CRITICAL"
elif abnormal_count > 0:
    overall_status = "ABNORMAL"
else:
    overall_status = "NORMAL"


print("\n=== FINAL DIAGNOSTIC REPORT ===")
print("Number of Processed Readings:", processed_count)
print("Valid Readings:", valid_count)
print("Invalid Readings:", invalid_count)
print("Detected Abnormal Conditions:", abnormal_count)
print("Critical Conditions:", critical_count)
print("Overall Equipment Status:", overall_status)