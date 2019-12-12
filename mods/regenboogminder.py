def run():
    aantal = 1000
    
    kleurtabel = []
    
    step = 4
    rood = 128
    blauw = 0
    groen = 0
    for i in range(0,128,step):
        groen = i
        kleurtabel += [ [rood, groen, blauw] ]
    for i in range(0,128,step):
        rood = 128 - i
        kleurtabel += [ [rood, groen, blauw] ]
    for i in range(0,128,step):
        blauw = i
        kleurtabel += [ [rood, groen, blauw] ]
    for i in range(0,128,step):
        groen = 128 - i
        kleurtabel += [ [rood, groen, blauw] ]
    for i in range(0,128,step):
        rood = i
        kleurtabel += [ [rood, groen, blauw] ]
    for i in range(0,128,step):
        blauw = 128 - i
        kleurtabel += [ [rood, groen, blauw] ]
    
    while len(kleurtabel) < aantal:
        kleurtabel += kleurtabel
    
    data = b""
    while True:
       for ledje in range(0,aantal):
           data += chr(kleurtabel[ledje][1]) + chr(kleurtabel[ledje][0]) + chr(kleurtabel[ledje][2])
       yield (0.2,data)
       data = b""
       x = kleurtabel.pop(0)
       kleurtabel = kleurtabel + [ x ]
