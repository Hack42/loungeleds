def run():
    global color,stopping
    while True:
        MESSAGE1 = "\x00\x00\x00" * 1200
        yield (1,MESSAGE1)
