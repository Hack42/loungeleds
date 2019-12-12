def colortable(width):
    kleurtabel = []

    step = 1530 / width
    rood = 255
    blauw = 0
    groen = 0
    for i in range(0,255,step):
        groen = i
        kleurtabel += [ [rood, groen, blauw] ]
    for i in range(0,255,step):
        rood = 255 - i
        kleurtabel += [ [rood, groen, blauw] ]
    for i in range(0,255,step):
        blauw = i
        kleurtabel += [ [rood, groen, blauw] ]
    for i in range(0,255,step):
        groen = 255 - i
        kleurtabel += [ [rood, groen, blauw] ]
    for i in range(0,255,step):
        rood = i
        kleurtabel += [ [rood, groen, blauw] ]
    for i in range(0,255,step):
        blauw = 255 - i
        kleurtabel += [ [rood, groen, blauw] ]
    return kleurtabel

