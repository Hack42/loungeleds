def run():
    global color
    MESSAGE1 = "\x00\x00\x00\x00\x00\x00" * 500
    MESSAGE2 = "\x00\x00\xff\x00\x00\xff" * 500
    for i in range(0,10):
        yield (0.1,MESSAGE1)
        yield (0.1,MESSAGE2)