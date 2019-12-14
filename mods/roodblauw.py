def run():
    MESSAGE1 = "\x00\x00\xff" * 790
    MESSAGE2 = "\xff\x00\x00" * 790
    for i in range(0,8):
        yield (0.2,MESSAGE1)
        yield (0.2,MESSAGE2)
