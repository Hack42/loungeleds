def run():
    aantal = 1000
    
    kleurtabel = []
    
    step = 4
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
    
    while len(kleurtabel) < aantal:
        kleurtabel += kleurtabel
    
    data = b""
    while True:
       for ledje in range(0,aantal):
           data += chr(kleurtabel[ledje][1]) + chr(kleurtabel[ledje][0]) + chr(kleurtabel[ledje][2])
       yield (0.05,data)
       data = b""
       x = kleurtabel.pop(0)
       kleurtabel = kleurtabel + [ x ]
