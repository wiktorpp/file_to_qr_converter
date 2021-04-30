# line 157 in pyqrcode needs to be changed from 
# "self.data = content.decode(encoding)" 
# to 
# "self.data = content", 
# else the program will error out

import pyqrcode
import sys
import bz2

#data = open(sys.argv[1], "rb").read()
print("Compressing...")
#data = bz2.compress(data)

data = bytes([0xff, 0xff, 0x00])

print(data)

#img = pyqrcode.create(data, version=27, mode='binary')
img = pyqrcode.create(data, error='L', mode='binary')
img.show()
#import pdb; pdb.set_trace()
#img.png(sys.argv[1]+".png")