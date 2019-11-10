import argparse
import time

def encoder(pscode):
    text = open(pscode).read()
    out = open(pscode[:pscode.index(".")] + ".bin", "w")
    txt = ""
    for i in text:
        txt += (bin(ord(i))[2:]+ ' ')
    out.write(txt[:-1])
    out.close()
    
def decoder(pscode):
    binary = open(pscode).read().split(" ")
    out = open(pscode[:pscode.index(".")] + ".p", "w")
    text = ""
    for i in binary:
        text += chr(int(i, base=2))
    out.write(text)
    out.close()
    
parser = argparse.ArgumentParser()
parser.add_argument("-e","--encode", metavar='FILE', help="Encode a ProtonScript program file.")
parser.add_argument("-d","--decode", metavar='FILE', help="Decode a ProtonScript program file.")
args = parser.parse_args()
    
if args.encode:
    print("ProtonScript Coder 3.0\n")
    time.sleep(1)
    import os
    import os.path
    if (os.path.exists(args.encode)):
        print("(1/2) Loading Program File ..... [ OK ]")
    else:
        print("(1/2) Loading Program File ..... [ FAIL ]\n")
        import sys
        sys.exit()
        
    if (os.path.exists("/data/data/com.termux")):
        pspath = "/data/data/com.termux/files/usr/bin/pscript"
    else:
        pspath = "/usr/local/bin/pscript"
        
    time.sleep(1)
            
    if (os.path.exists(pspath)):
        print("(2/2) Loading ProtonScript  .....  [ OK ]\n")
    else:
        print("(2/2) Loading ProtonScript  .....  [ FAIL ]\n")
        import sys
        sys.exit()
    
    encoder(args.encode)
    
if args.decode:
    print("ProtonScript Coder 3.0\n")
    time.sleep(1)
    import os
    import os.path
    if (os.path.exists(args.decode)):
        print("(1/2) Loading Program File ..... [ OK ]")
    else:
        print("(1/2) Loading Program File ..... [ FAIL ]\n")
        import sys
        sys.exit()
        
    if (os.path.exists("/data/data/com.termux")):
        pspath = "/data/data/com.termux/files/usr/bin/pscript"
    else:
        pspath = "/usr/local/bin/pscript"
        
    time.sleep(1)
            
    if (os.path.exists(pspath)):
        print("(2/2) Loading ProtonScript  .....  [ OK ]\n")
    else:
        print("(2/2) Loading ProtonScript  .....  [ FAIL ]\n")
        import sys
        sys.exit()
    
    decoder(args.decode)
