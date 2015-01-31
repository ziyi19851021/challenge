from PIL import Image
import PIL
import Image

im = Image.open('./oxygen.png')
pixel =im.getcolors(maxcolors=256)
size = im.size
print im.size,im.format,im.mode
print size

rgb_im = im.convert('RGB')
r, g, b = rgb_im.getpixel((1, 1))

print r, g, b
r, g, b = rgb_im.getpixel((628, 94))
print r, g, b

#for i in range(95):
#    r, g, b = rgb_im.getpixel((1, i))
#    print r, g, b , i

key= ['115']
i = 0
for j in range(607):
    r, g, b = rgb_im.getpixel((j, 46))
    if  len(key)== 0 or r != key[i]:
        key.append(r)    
        #print r, g, b , j
        print chr(int(r)),
        i += 1

key2 = [105,110,116,101,103,114,105,116,121]
print ""
for i in range(len(key2)):
    print chr(key2[i]),

               




