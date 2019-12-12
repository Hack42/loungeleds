color = "\xff\xff\xff"
def run():
    global color
    MESSAGE1 = "\x00\x00\x00" * 1000
    MESSAGE2 = color * 1000
    for i in range(0,10):
        yield (0.2,MESSAGE1)
        yield (0.2,MESSAGE2)
