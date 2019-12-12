def run():
    global color,stopping
    while True:
        MESSAGE1 = "\xff\x00\x00" * 1000
        yield (1,MESSAGE1)
