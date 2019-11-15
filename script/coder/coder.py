import argparse
import time
import os

def encoder(pscode):
    text = open(pscode).read()
    out = open(pscode[:pscode.index(".")] + ".bin", "w")
    txt = ""
    for i in text:
        txt += (bin(ord(i))[2:]+ ' ')
    out.write(txt[:-1])
    out.close()
    os.system("rm "+pscode)
    
def decoder(pscode):
    binary = open(pscode).read().split(" ")
    out = open(pscode[:pscode.index(".")] + ".p", "w")
    text = ""
    for i in binary:
        text += chr(int(i, base=2))
    out.write(text)
    out.close()
    os.system("rm "+pscode)
    
parser = argparse.ArgumentParser()
parser.add_argument("-e","--encode", metavar='FILE', help="Encode a ProtonScript program file.")
parser.add_argument("-d","--decode", metavar='FILE', help="Decode a ProtonScript program file.")
args = parser.parse_args()
    
if args.encode:
    argrem = args.encode
    time.sleep(1)
    import os
    import os.path
    if (os.path.exists(args.encode)):
        if (argrem[-(argrem[::-1].index('.')):]) != 'p':
            print("(1/4) Loading Program File ..... [ FAIL ]\n")
            import sys
            sys.exit()
        else:
            print("(1/4) Loading Program File  ..... [ OK ]")
    else:
        print("(1/4) Loading Program File ..... [ FAIL ]\n")
        import sys
        sys.exit()
        
    if (os.path.exists("/data/data/com.termux")):
        pspath = "/data/data/com.termux/files/usr/bin/pscript"
    else:
        pspath = "/usr/local/bin/pscript"
        
    time.sleep(1)
            
    if (os.path.exists(pspath)):
        print("(2/4) Loading ProtonScript  ..... [ OK ]")
    else:
        print("(2/4) Loading ProtonScript ..... [ FAIL ]\n")
        import sys
        sys.exit()
    
    print("(3/4) Encoding Program File ..... [ OK ]")
    time.sleep(2)
    encoder(args.encode)
    print("(4/4) Saving Program File   ..... [ OK ]")
    time.sleep(2)
    print("")
    import sys
    sys.exit()
    
if args.decode:
    argrem = args.decode
    time.sleep(1)
    import os
    import os.path
    if (os.path.exists(args.decode)):
        if (argrem[-(argrem[::-1].index('.')):]) != 'bin':
            print("(1/4) Loading Program File ..... [ FAIL ]\n")
            import sys
            sys.exit()
        else:
            print("(1/4) Loading Program File  ..... [ OK ]")
    else:
        print("(1/4) Loading Program File ..... [ FAIL ]\n")
        import sys
        sys.exit()
        
    if (os.path.exists("/data/data/com.termux")):
        pspath = "/data/data/com.termux/files/usr/bin/pscript"
    else:
        pspath = "/usr/local/bin/pscript"
        
    time.sleep(1)
            
    if (os.path.exists(pspath)):
        print("(2/4) Loading ProtonScript  ..... [ OK ]")
    else:
        print("(2/4) Loading ProtonScript ..... [ FAIL ]\n")
        import sys
        sys.exit()
    
    print("(3/4) Decoding Program File ..... [ OK ]")
    time.sleep(2)
    decoder(args.decode)
    print("(4/4) Saving Program File   ..... [ OK ]\n")
    time.sleep(2)
    print("")
    import sys
    sys.exit()
