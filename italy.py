import PIL,Image,sys
sys.setrecursionlimit(1000000)

global im
global im2
global i
global x 
global y
global li
im = Image.open("wire.png")
im2 = Image.new("RGB",(100,100),(255,255,255))   
i = 0
x = 0
y = 0
li = [(0,0)]

def curve():
    if (x+1, y) not in li and x <99:
        right()
    if (x, y+1) not in li and y < 99:
        down()
    if (x-1, y) not in li and x > 0: 
        left()
    if (x, y -1) not in li and y> 0:
        up()
    return 1

def right():
    global im
    global im2
    global i
    global x 
    global y
    global li
    print x,",",y
    if (x+1, y) not in li and x <99:
        x = x + 1
        li.append((x,y))   
        pix = im.getpixel((i,0))
        im2.putpixel((x,y),pix)
        i += 1
        right()
    else:
        curve()
    return 1
        
def down():
    global im
    global im2
    global i
    global x 
    global y
    global li
    print x,",",y
    if (x, y+1) not in li and y < 99:
        y = y + 1
        li.append((x,y))   
        pix = im.getpixel((i,0))
        im2.putpixel((x,y),pix)
        i += 1
        down()
    else:
        curve()
    return 1
def left():
    global im
    global im2
    global i
    global x 
    global y
    global li
    print x,",",y
    if (x-1, y) not in li and x > 0: 
        x = x - 1
        li.append((x,y))   
        pix = im.getpixel((i,0))
        im2.putpixel((x,y),pix)
        i += 1
        left()
    else:
        curve()
    return 1
def up():
    global im
    global im2
    global i
    global x 
    global y
    global li
    print x,",",y
    if (x, y -1) not in li and y> 0:
        y = y- 1
        li.append((x,y))   
        pix = im.getpixel((i,0))
        im2.putpixel((x,y),pix)
        i += 1
        up()
    else:
        curve()
    return 1



'''im = Image.open("wire.png")
print im.size


width = 100
bgcolor = (255, 255, 255)
im2 = Image.new("RGB",(width,width),bgcolor)
flag = 1
j = 0

for i in range(1000):
    pix = im.getpixel((i,0))
#    im2.putpixel((i%100,i/100),pix)
    im2.putpixel((j,i/100),pix)
    if flag :
        j += 1
        if j == 100:
            j = 99
            flag = 0
    else:
        j -=1
        if j == -1:
            j = 0
            flag = 1'''

    
if __name__ == "__main__":


    curve()
    im2.save("1122.png")
