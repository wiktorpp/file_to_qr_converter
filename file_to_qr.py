# line 157 in pyqrcode needs to be changed from 
# "self.data = content.decode(encoding)" 
# to 
# "self.data = content", 
# else the program will error out

import sys
import bz2
import pyqrcode

data = open(sys.argv[1], "rb").read()
n = 1003
chunks = [data[i:i+n] for i in range(0, len(data), n)]
for i, chunk in enumerate(chunks):
    img = pyqrcode.create(chunk, error='L', mode='binary')
    #img.show()
    img.png(f"{sys.argv[1]}.pt{str(i)}.png")
