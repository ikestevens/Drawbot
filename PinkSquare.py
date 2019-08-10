RECTSIZE = 6
CANVAS = 500
NFRAMES = 120
MID = 59.5
TRUEMID = 60.5

def IncreaseRotate(t):
    size = (t + MID) * RECTSIZE
    return size

def IncreaseTiny(t):
    if t < 1:
        size = 0
    else:
        size = ((t) * RECTSIZE)
    return size

def IncreaseLast(t):
    if t < MID:
        size = 0
    else:
        size = ((t - TRUEMID) * RECTSIZE)
    return size

for i in range(NFRAMES):
    newPage(CANVAS, CANVAS)
    frameDuration(1/20)
    translate(CANVAS/2, CANVAS/2)
    fill(1)
    rect(-CANVAS/2, -CANVAS/2, CANVAS, CANVAS)

    #Pink Square
    fill(1, 0, 0, .5)
    stroke(0)
    bigSize = IncreaseRotate(i)
    rotate(3 * i)
    rect(-bigSize/2, -bigSize/2, bigSize, bigSize)

#White Square
    fill(1)
    stroke(0)
    sqSize = IncreaseTiny(i)
    rect(-sqSize/2, -sqSize/2, sqSize, sqSize)

#Pink Square
    fill(1, 0, 0, .5)
    stroke(0)
    lastSize = IncreaseLast(i)
    rect(-lastSize/2, -lastSize/2, lastSize, lastSize)


saveImage("PinkSquare.gif")
