import ndspy.lz10, sys, os

def decompress(file):

    filename = os.path.basename(file)

    file = open(filename, "rb")

    filedata = file.read()

    filedata = ndspy.lz10.decompress(filedata)

    newfile = open(f"decmp_{filename}", "wb")

    newfile.write(filedata)

def compress(file):
     
    filename = os.path.basename(file)

    file = open(filename, "rb")

    filedata = file.read()

    filedata = ndspy.lz10.compress(filedata)

    newfile = open(f"{filename}_cmp", "wb")

    newfile.write(filedata)

if __name__ == "__main__":
        if len(sys.argv) != 3:
            print("Usage: python summ.py [compress/decompress] file")
            sys.exit(1)

        if (sys.argv[1] == "compress"):
            compress(sys.argv[2])
        
        elif(sys.argv[1] == "decompress"):
            decompress(sys.argv[2])
        
        else:
            print("Usage: python summ.py [compress/decompress] file")
            sys.exit(1)
             
    

