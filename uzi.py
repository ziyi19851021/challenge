import time

print time.time()
date = "26 Jan "
for i in range(1006,1997,10):
    if time.strptime("26 Jan "+str(i), "%d %b %Y").tm_wday == 0 and i%4 == 0:
        print i
print time.strptime("29 Feb 1816", "%d %b %Y").tm_wday 

