LAST_NAME = "ALDOVINO"
SEED_NUM = 8
FAVORITE_ARTIST = "BINI"


def generate_fault_code(last_name, seed_num, artist):
    name_value = sum(ord(char) for char in last_name)
    artist_value = sum(ord(char) for char in artist)

    fault_code = (name_value + artist_value + seed_num) % 9000 + 1000

    return fault_code


recursive_calls = 0


def trace_fault(code, trace=None):
    global recursive_calls

    if trace is None:
        trace = []

    recursive_calls += 1
    trace.append(code)

    # Base condition
    if code < 10:
        return trace

    # Recursive call
    return trace_fault(code // 10, trace)


print("=== RECURSIVE FAULT TRACE ===")
print("Engineer:", LAST_NAME)
print("Seed Number:", SEED_NUM)
print("Favorite Artist:", FAVORITE_ARTIST)

fault_code = generate_fault_code(
    LAST_NAME,
    SEED_NUM,
    FAVORITE_ARTIST
)

print("\nGenerated Fault Data:")
print("Fault Code:", fault_code)

print("\n[LOG] Starting recursive fault trace...")

fault_trace = trace_fault(fault_code)

print("[LOG] Recursive fault trace completed.")

print("\nRecursive Trace:")
for level, value in enumerate(fault_trace, start=1):
    print(f"Level {level}: {value}")

print("\nNumber of Recursive Calls:")
print(recursive_calls)

print("\nFinal Result:")
print("Final Fault Value:", fault_trace[-1])