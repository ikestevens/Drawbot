RECTSIZE = 6
CANVAS = 500
NFRAMES = 120
MID = 59.5
TRUEMID = 60.5

def IncreaseFirst(t):
    size = (t + MID) * RECTSIZE
    return size

def IncreaseSecond(t):
    #This square is size zero until 1 frame in
    if t < 1:
        size = 0
    else:
        size = ((t) * RECTSIZE)
    return size

def IncreaseLast(t):
    #This square is size zero until mid-way into the gif (60 frames)
    if t < MID:
        size = 0
    else:
        size = ((t - TRUEMID) * RECTSIZE)
    return size

for i in range(NFRAMES):
    #Set the background and set origin to center
    newPage(CANVAS, CANVAS)
    frameDuration(1/20)
    translate(CANVAS/2, CANVAS/2)
    fill(0)
    rect(-CANVAS/2, -CANVAS/2, CANVAS, CANVAS)

    #This rotate function creates the spin of the gif
    rotate(3 * i)

    #Create length of First Square
    bigSize = IncreaseFirst(i)

    #Draw the lines outside the square at the beginning
    stroke(1)
    strokeWidth(.01)
    line((300, 300), (bigSize/2, bigSize/2))
    stroke(1)
    strokeWidth(.01)
    line((-300, 300), (-bigSize/2, bigSize/2))
    stroke(1)
    strokeWidth(.01)
    line((300, -300), (bigSize/2, -bigSize/2))
    stroke(1)
    strokeWidth(.01)
    line((-300, -300), (-bigSize/2, -bigSize/2))

    #Draw First Square
    fill(1)
    rect(-bigSize/2, -bigSize/2, bigSize, bigSize)

    #Draw Lines Inside First Square
    stroke(0)
    strokeWidth(.01)
    line((0,0), (bigSize/2, bigSize/2))
    stroke(0)
    strokeWidth(.01)
    line((0,0), (-bigSize/2, bigSize/2))
    stroke(0)
    strokeWidth(.01)
    line((0,0), (bigSize/2, -bigSize/2))
    stroke(0)
    strokeWidth(.01)
    line((0,0), (-bigSize/2, -bigSize/2))


    #Second Square (Black)
    fill(0)
    sqSize = IncreaseSecond(i)
    rect(-sqSize/2, -sqSize/2, sqSize, sqSize)

    #Draw lines inside second square
    stroke(1)
    strokeWidth(.01)
    line((0,0), (sqSize/2, sqSize/2))
    stroke(1)
    strokeWidth(.01)
    line((0,0), (-sqSize/2, sqSize/2))
    stroke(1)
    strokeWidth(.01)
    line((0,0), (sqSize/2, -sqSize/2))
    stroke(1)
    strokeWidth(.01)
    line((0,0), (-sqSize/2, -sqSize/2))

    #Last Square, which transitions to the first square
    fill(1)
    lastSize = IncreaseLast(i)
    rect(-lastSize/2, -lastSize/2, lastSize, lastSize)

    #Last Square lines
    stroke(0)
    strokeWidth(.01)
    line((0,0), (lastSize/2, lastSize/2))
    stroke(0)
    strokeWidth(.01)
    line((0,0), (-lastSize/2, lastSize/2))
    stroke(0)
    strokeWidth(.01)
    line((0,0), (lastSize/2, -lastSize/2))
    stroke(0)
    strokeWidth(.01)
    line((0,0), (-lastSize/2, -lastSize/2))

saveImage("RotatingSquares.gif")
