#/usr/bin/env python 

import Image, sys
sys.setrecursionlimit(1000000)

(bw, bh) = (639, 0)
(fw, fh) = (1, 640)
path = [(0, 0)]
opath = []
rpath = []
gap = 1
end = 0

def step((w, h)):
	print (w, h)
	global end
	global rpath
	global opath
	global path
	if w-gap>=0 and map[w-gap][h] == 0 and end == 0:
		if (w - gap, h) not in path and (w - gap, h) not in opath:		
			w = w - gap
			path.append((w, h))
			step((w, h)) 
			if end == 0:
				w = w + gap
				path.pop()

	if h+gap < 641 and map[w][h + gap]==0 and end == 0:
		if (w, h+gap) not in path and (w, h + gap) not in opath:
			h = h + gap
			path.append((w, h))
			step((w, h))
			if end == 0:
				h = h - gap
				path.pop()

	if w+gap<641 and map[w+gap][h] == 0 and end == 0:
		if (w+gap,h) not in path and (w + gap, h) not in opath:		
			w = w + gap
			path.append((w, h))
			step((w, h)) 
			if end == 0:
				w = w - gap
				path.pop()

	if h-gap>=0 and map[w][h-gap] == 0 and end == 0:
		if (w, h-gap) not in path and (w,h-gap) not in opath:		
			h = h - gap
			path.append((w, h))
			step((w, h)) 
			if end == 0:
				h = h + gap
				path.pop()

	if (w, h) == (1, 640):
		rpath = path
		end = 1
		print rpath
	print "Trace back"
	opath.append((w, h))
	return 

def Makemap(path):
	im = Image.open(path)	
	im_rgb = im.convert('RGB')
	print path
	map = []
	for i in range(im.size[0]):
		map.append([])
		for j in range(im.size[1]):
			map[i].append(im_rgb.getpixel((i, j)))
	return map

def begin_end():
	im = Image.open('./maze.png')
	im_rgb = im.convert('RGB')
	for i in range(im.size[0]):
		if im_rgb.getpixel((i, 0))[2] == 0:
			(bw, bh) = (i, 0)
			print 'b=',(bw,bh)
		if im_rgb.getpixel((i, im.size[1]-1)) == (255, 255, 255):
			print (i, im.size[1]-1)
			(fw, fh) = (i, im.size[1]-1)
			print 'f=',(fw, fh)
		
def saveaspic():
	for i in range(len(rpath)):
		im_rgb.putpixel(rpath[i],(0, 0, 255))
	im_rgb.save('maze2.png')	

def findinf(map):
	x = 639
	y = 0
	enpath = []
	fcontent = []
	while (x, y) != (1, 640):
		print (x, y)
#		print fcontent
		if x < 640 and (x+1, y) not in enpath and map[x+1][y][2] == 0: 
			x = x + 1
			fcontent.append(map[x][y][0])
			enpath.append((x, y))
		if x > 0 and (x-1, y) not in enpath and map[x-1][y][2] == 0:
			x = x - 1
			fcontent.append(map[x][y][0])
			enpath.append((x, y))
		if y<640 and (x,y+1) not in enpath and map[x][y+1][2] == 0:
			y = y + 1
			fcontent.append(map[x][y][0])
			enpath.append((x, y))
		if y>0 and (x,y-1) not in enpath and map[x][y-1][2] == 0:
			y = y - 1
			fcontent.append(map[x][y][0])
			enpath.append((x, y))
	return fcontent

def saveaszip(fcontent):
	f = open('ambiguity.zip', 'wb')
	for i in fcontent[0::2]:
#		print i
		f.write(chr(i))	
	f.close()

def rewritemap():
	im = Image.open('maze2.png')	
	im_rgb = im.convert('RGB')
	im0 = Image.open('maze.png')
	im_rgb0 = im0.convert('RGB') 
	for i in range(im.size[0]):
		for j in range(im.size[1]):
			con = im_rgb.getpixel((i, j))
			if (con[1],con[2])!=(0, 255):
				im_rgb.putpixel((i,j),(255,255,255))
			else:
				im_rgb.putpixel((i,j),im_rgb0.getpixel((i,j)))
	im_rgb.save('maze3.png')

if __name__ == "__main__":
	print 'initial'
	map = Makemap("maze3.png")
	print 'start'
#	fcontent = [1,2,3]
	fcontent = findinf(map)	
	print 'write'
	saveaszip(fcontent)
	#rewritemap()
	'''
	What?
	This is a programm tha try to find the way out of the riddle.In the riddle,every red digtel is a information about artibory . ZIP header is PK. then write it in ZIP with file,and open it. You will find the answer.
	How?
	There are servel functions in the programm.each of them have different function Makemap() is to make png change to the list.I thought it will be quick for my raspberry. steps() is to find the way out the maze black is the way and white is the wall.Saveaspic() is the way to save the result. findinfo() is mean to find the red information for file . And save as ZIP is to write it in ZIP file.
	'''
