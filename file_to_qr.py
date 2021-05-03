compress = False

import sys
import bz2
import segno

data = open(sys.argv[1], "rb").read()
if compress:
    data = bz2.compress(data)
n = 1003
chunks = [data[i:i+n] for i in range(0, len(data), n)]
for i, chunk in enumerate(chunks):
    img = segno.make(chunk, micro=False)
    #img.show()
    img.save(f"{sys.argv[1]}{'.bz2' if compress else ''}.pt{str(i)}.png")
