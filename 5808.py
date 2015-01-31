import PIL
import Image

im = Image.open("./cave.jpg")
im.getdata() 
r,g,b = im.split()  

mylist = []

width = 320

 
height = 240  
 
bgcolor = (255,255,255)  
imagea = Image.new('RGB',(width,height),bgcolor)
imageb = Image.new('RGB',(width,height),bgcolor)
print im.size

for i in range(0,640,2):
    for j in range(0,480,2):
        imagea.putpixel((i/2,j/2),im.getpixel((i,j)))
imagea.save('11.jpg')
for i in range(1,640,2):
    for j in range(1,480,2):
        imageb.putpixel((i/2,j/2),im.getpixel((i,j)))
imageb.save('22.jpg')      

