from pathlib import Path
import sys, os
binPath = Path(sys.argv[1]).resolve()

binFile = open(binPath, "rb")
outFolder = str(binPath).removesuffix(".bin")
os.makedirs((binPath / outFolder), exist_ok=True)

def readint(b: bytes) -> int:
    return int.from_bytes(b, byteorder="little")

count = readint(binFile.read(4))
start = readint(binFile.read(4))
mult = readint(binFile.read(4))
shift = readint(binFile.read(4))
mask = readint(binFile.read(4))

print(f"{count:X} {start:X} {mult:X} {shift:X} {mask:X} ")

fileinfo = []

for i in range(count):
    
    val1 = readint(binFile.read(4))

    offset = val1 >> shift
    offset = offset * start

    newval = val1 & mask
    newval = newval * mult
    newval = newval + start
    newval = newval - 1

    size = newval // start
    size = size * start

    print(f"{val1:X} {offset:X} {size:X}")

    fileinfo.append([offset, size])

for i in range(count):

    binFile.seek(fileinfo[i][0])
    data = binFile.read(fileinfo[i][1])

    newfile = open(f"{binPath / outFolder}//file{i}.bin", "wb")
    newfile.write(data)
    newfile.close()

#  FUN_001057c8