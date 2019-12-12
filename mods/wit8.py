def run():
    global color,stopping
    while True:
        MESSAGE1 = "\x8f\x8f\x8f" * 1000
        yield (1,MESSAGE1)
