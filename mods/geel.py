def run():
    global color
    MESSAGE1 = "\x00\x00\x00\xff\xff\x00" * 500
    MESSAGE2 = "\xff\xff\x00\x00\x00\x00" * 500
    for i in range(0,8):
        yield (0.6,MESSAGE1)
        yield (0.6,MESSAGE2)
