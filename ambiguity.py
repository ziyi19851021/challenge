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
		if x < 640 and (x+1, y) not in enpath and (map[x+1][y][1],map[x+1][y][2]) == (0, 255): 
			x = x + 1
			fcontent.append(map[x][y][0])
			enpath.append((x, y))

		if x>0 and (x-1,y) not in enpath and (map[x-1][y][1],map[x-1][y][2]) == (0, 255):
			x = x - 1
			fcontent.append(map[x][y][0])
			enpath.append((x, y))

		if y<640 and (x,y+1) not in enpath and (map[x][y+1][1],map[x][y+1][2]) == (0, 255):
			y = y + 1
			fcontent.append(map[x][y][0])
			enpath.append((x, y))
		if y>0 and (x,y-1) not in enpath and (map[x][y-1][1],map[x][y-1][2]) == (0, 255):
			y = y - 1
			fcontent.append(map[x][y][0])
			enpath.append((x, y))
	return fcontent

def saveaszip(fcontent):
	file = open('ambiguity.zip', 'wb')
	for i in range(len(fcontent)):
		if fcontent[i] != 0:
			file.write(fcontent[i])	
	file.close()

if __name__ == "__main__":
	print 'initial'
#	map = Makemap("maze2.png")
	print 'start'
#	fcontent = findinf(map)	
	fcontent = [1,2,3]
	saveaszip(fcontent)
	

	
