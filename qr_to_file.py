import sys
import bz2

if len(sys.argv) != 2: raise ValueError("Filename not specified")
if not sys.argv[1].endswith(".csv"): raise ValueError('Wrong file format (not ".csv"), please supply output from Binary Eye (CSV file with semicolons)')

csv = reversed(open(sys.argv[1], 'r').read().split('\n')[1:-1])
output = b''
#print(list(csv))
for line in csv:
    line = line.replace('"', '').split(";")
    #print(line)
    if line[1] != 'QR_CODE':
        print(f"error: {line[2]} not qr code, skipping")
        continue
    try:
        data = bytes.fromhex(line[2])
        output += data
    except ValueError:
        print(f'error: "{line[2]}" not hex, skipping')

#print(output)
print("Decompressing...")
try:
    output = bz2.decompress(output)
except:
    print("Failed to decompress, data not comopressed")
print("Writing: " + sys.argv[1].split(".csv")[0])
open(sys.argv[1].replace(".csv", ""), "wb").write(output)