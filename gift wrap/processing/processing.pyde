from random import gauss as rand
import cmath

SIZE = 720
color_bg = "#EBF2FA"
color_hull = "#427AA1"
color_curr = "#679436"
color_gray = "#BBBBBB"
color_gold = "#F0A202"
    
def random_points(size, n):
    global leftmost
    points = []
    for _ in range(n):
        x, y = rand(size/2, 150), rand(size/2, 150)
        if (0<x<size) and (0<y<size):
            points.append(x + y*1j)
    leftmost = sorted(points, key = lambda z: z.real)[0]
    return points

def cross(z1, z2, ref): # this complex number expression evauluates to vector cross product
    z1 = z1-ref
    z2 = z2 - ref
    return (z1 * z2.conjugate() - z1.conjugate() * z2).imag

def setup():
    global leftmost, currvert, nextvert, i, hull
    global points
    background(color_bg)
    size(SIZE,SIZE)
    points = random_points(SIZE, 50)
    i = 0
    currvert = leftmost
    nextvert = points[0]
    hull = [] # initiate hull
    hull.append(leftmost) # add leftmost to hull
    
def draw():
    background(color_bg)
    global i, nextvert, hull, currvert, points
    
    
    # -------- draw all points
    
    for p in points:
        stroke(color_gold)
        strokeWeight(10)
        point(p.real, p.imag)
        
        
        
    # -------- draw current vertex
    
    strokeWeight(20)
    stroke(color_curr)
    point(currvert.real, currvert.imag)
    
    
    
    # -------- draw hull
    
    stroke(color_hull)
    strokeWeight(2)
    noFill()
    beginShape()
    for p in hull:
        vertex(p.real, p.imag)
    endShape()
    
    
    
    # --------- draw line joining current vertex and next vertex
    
    strokeWeight(2)
    stroke(color_curr)
    line(currvert.real, currvert.imag, nextvert.real, nextvert.imag)
    
    # --------  draw line joining next vertex to the candidate next vertex (checking vertex)
    checking = points[i]
    stroke(color_gray)
    strokeWeight(2)
    line(nextvert.real, nextvert.imag, checking.real, checking.imag)
    
    
    
    # check if candidate point is on hull
    
    checking = points[i]
    if (nextvert != currvert and # gotta check otherwise Zero div error
        checking != nextvert and
        cross(checking, nextvert, currvert) < 0): # candidate is on left
        nextvert = checking
        
    if i == len(points)-1:
        if nextvert == leftmost:
            noLoop()
        i = 0
        hull.append(nextvert)
        currvert = nextvert 
        nextvert = points[i]

        # noLoop()
        
    else:
        i += 1
        
        
    frameRate(60)
    
    # print(hull)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
