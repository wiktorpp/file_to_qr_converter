# line 157 in pyqrcode needs to be changed from 
# "self.data = content.decode(encoding)" 
# to 
# "self.data = content", 
# else the program will error out

compress = True

import sys
import bz2
import pyqrcode

data = open(sys.argv[1], "rb").read()
if compress:
    data = bz2.compress(data)
n = 1003
chunks = [data[i:i+n] for i in range(0, len(data), n)]
for i, chunk in enumerate(chunks):
    img = pyqrcode.create(chunk, error='L', mode='binary')
    #img.show()
    img.png(f"{sys.argv[1]}{'.bz2' if compress else ''}.pt{str(i)}.png")
