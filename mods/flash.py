color = "\xff\xff\xff"
def run():
    global color
    MESSAGE1 = "\x00\x00\x00" * 200
    MESSAGE2 = color * 200
    for i in range(0,10):
        yield (0.1,MESSAGE1)
        yield (0.1,MESSAGE2)
