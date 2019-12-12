def run():
    global color,stopping
    while True:
        MESSAGE1 = "\x00\xff\x00" * 1000
        yield (1,MESSAGE1)
