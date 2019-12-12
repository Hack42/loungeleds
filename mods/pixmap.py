#!/usr/bin/python3
startx = 48
starty = 21
lastpixel = 0
def pixmap():
    pixmap = []
    for y in range(0,50):
      pixmap.append( [-1] * 70)
    
    def run(left,down,pixel):
        global startx,starty,lastpixel
        i = 0
        for i in range(lastpixel + (1 if lastpixel else 0),pixel):
            pixmap[starty][startx]=i
            startx = startx + (-1 if left < 0 else (1 if left else 0))
            starty = starty + (-1 if down < 0 else (1 if down else 0))
        lastpixel = i
    
    run(-3,0,25);
    run(0,1,33);
    run(4,0,63);
    run(0,-2,79);
    run(-5,0,118);
    run(0,3,141);
    run(6,0,187);
    run(0,-4,216);
    run(-7,0,268);
    run(0,5,306);
    run(8,0,367);
    run(0,-6,412);
    run(-9,0,481);
    run(0,7,531);
    
    #for line in pixmap:
    #  print("".join(["%03d " % x if x != -1 else '... ' for x in line]))
    
    pixels = {}
    for y in range(0,50):
        for x in range(0,70):
            if pixmap[y][x] != -1:
                pixels[pixmap[y][x]] = (x,y)
    return pixels

