from random import randint
def run():
    global color,stopping
    while True:
        x = randint(0,790)
        MESSAGE1 = "\x1f\x1f\x1f" * x + "\xFF\xFF\xFF" + "\x1f\x1f\x1f" * (790 - x)
        yield (0.1,MESSAGE1)
        MESSAGE1 = "\x1f\x1f\x1f" * 790
        yield (0.5,MESSAGE1)
