def run():
    global color,stopping
    while True:
        MESSAGE1 = "\xff\xff\xff" * 200
        yield (1,MESSAGE1)
