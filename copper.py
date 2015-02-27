#/usr/bin/env python

import PIL,Image 

im = Image.open('./white.gif')
im_rgb = im.convert('RGB') 
for i in range(0, im.size[0]):
	for j in range(0, im.size[1]):
		if im_rgb.getpixel((i, j)) != (0,0,0):
			print im_rgb.getpixel((i,j)), (i, j)
			im_list = [(i,j)]
while 1:
	try:
		#print im.tell()
		im.seek(im.tell()+1)
		im_rgb = im.convert('RGB')
		for i in range(98,103):
			for j in range(98,103):
				if im_rgb.getpixel((i,j))!=(0,0,0):
					print im_rgb.getpixel((i,j)),(i,j)
					im_list.append((i,j))	
					continue
	except:
		break	


im_new = Image.new('RGB', (170,170), (0,0,0))
height = 20
wight = 20
for n in range(0 , len(im_list)):
	im_new.putpixel((height,wight),(n,255,255))
	half_height = (im_list[n][0] - 100)/2
	half_weight = (im_list[n][1] - 100)/2
	im_new.putpixel((height+half_height,wight+half_weight),(n,255,255))
	height = height + im_list[n][0] - 100
	wight = wight + im_list[n][1] -100
	if half_height == 0:
		if half_weight == 0:
			height = height +20
			wight = wight +20	
	print (height , wight)
im_new.save("./white.jpg")
print len(im_list)
