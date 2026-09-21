def generate_telemetry(last_name, seed_num, artist):
    base = sum(ord(char) for char in last_name) + seed_num
    artist_value = sum(ord(char) for char in artist)

    values = [
        (base + artist_value) % 61,
        (base + artist_value + 7) % 61,
        (base + artist_value + 14) % 61,
        (base + artist_value + 21) % 61,
        (base + artist_value + 28) % 61,
        (base + artist_value + 35) % 61,
        (base + artist_value + 42) % 61,
        (base + artist_value + 49) % 61
    ]

    for value in values:
        yield value