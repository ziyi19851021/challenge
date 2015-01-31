import PIL,Image

im = open("./evil2.gfx","rb")

list1 = []
f1 = open("./1.jpg", 'wb')
f2 = open("./2.jpg", 'wb')
f3 = open("./3.jpg", 'wb')
f4 = open("./4.jpg", 'wb')
f5 = open("./5.jpg", 'wb')

list1=im.read()
    
print len(list1)

for j in range(0,len(list1),5):
    f1.write(list1[j])
    
for j in range(1,len(list1),5):
    f2.write(list1[j])
for j in range(2,len(list1),5):
    f3.write(list1[j])
for j in range(3,len(list1),5):
    f4.write(list1[j])
for j in range(4,len(list1),5):
    f5.write(list1[j])

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()


