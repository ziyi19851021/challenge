#/usr/bin/env python

import PIL,Image

im = Image.open("./mozart.gif")
im_rgb = im.convert("RGB")
im_new = Image.new("RGB",(1280,480),(255,255,255))
add = 0
print im.size
for y in range(480):
	x = 0
	print y
	for i in range(640):
		if im_rgb.getpixel((i,y)) == (255,0,255):
			add = i
#		print im_rgb.getpixel((i,0))
	for i in range(640-add,1280-add):
		im_new.putpixel((i,y),im_rgb.getpixel((x,y)))
		x += 1
im_new.save("xxx.jpg")
