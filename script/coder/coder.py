import argparse
import time
import os

G = "\033[1m"
R = "\033[1m"
E = "\033[0m"

def encoder(pscode):
    text = open(pscode).read()
    out = open(pscode[:pscode.index(".")] + ".psc", "w")
    if text == '':
        out.write('')
        os.system("rm "+pscode)
        return None
    txt = ""
    for i in text:
        txt += (bin(ord(i))[2:]+ ' ')
    out.write(txt[:-1])
    out.close()
    os.system("rm "+pscode)
    
def decoder(pscode):
    binary = open(pscode).read()
    out = open(pscode[:pscode.index(".")] + ".p", "w")
    if binary == '':
        out.write('')
        os.system("rm "+pscode)
        return None
    binary = binary.split(" ")
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
        if '.' in args.encode:
            time.sleep(0)
        else:
            print("\n(1/4) Loading Program File ..... [ "+R+"FAIL"+E+" ]\n")
            import sys
            sys.exit()
            
        if (argrem[-(argrem[::-1].index('.')):]) == 'p':
            print("\n(1/4) Loading Program File  ..... [ "+G+"OK"+E+" ]")
            
        else:
            print("\n(1/4) Loading Program File ..... [ "+R+"FAIL"+E+" ]\n")
            import sys
            sys.exit()
    else:
        print("\n(1/4) Loading Program File ..... [ "+R+"FAIL"+E+" ]\n")
        import sys
        sys.exit()
        
    if (os.path.exists("/data/data/com.termux")):
        pspath = "/data/data/com.termux/files/usr/bin/pscript"
    else:
        pspath = "/usr/local/bin/pscript"
        
    time.sleep(1)
            
    if (os.path.exists(pspath)):
        print("(2/4) Loading ProtonScript  ..... [ "+G+"OK"+E+" ]")
    else:
        print("(2/4) Loading ProtonScript ..... [ "+R+"FAIL"+E+" ]\n")
        import sys
        sys.exit()
    
    print("(3/4) Encoding Program File ..... [ "+G+"OK"+E+" ]")
    time.sleep(2)
    encoder(args.encode)
    print("(4/4) Saving Program File   ..... [ "+G+"OK"+E+" ]")
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
        if '.' in args.decode:
            time.sleep(0)
        else:
            print("\n(1/4) Loading Program File ..... [ "+R+"FAIL"+E+" ]\n")
            import sys
            sys.exit()
            
        if (argrem[-(argrem[::-1].index('.')):]) == 'psc':
            print("\n(1/4) Loading Program File  ..... [ "+G+"OK"+E+" ]")
            
        else:
            print("\n(1/4) Loading Program File ..... [ "+R+"FAIL"+E+" ]\n")
            import sys
            sys.exit()
    else:
        print("\n(1/4) Loading Program File ..... [ "+R+"FAIL"+E+" ]\n")
        import sys
        sys.exit()
        
    if (os.path.exists("/data/data/com.termux")):
        pspath = "/data/data/com.termux/files/usr/bin/pscript"
    else:
        pspath = "/usr/local/bin/pscript"
        
    time.sleep(1)
            
    if (os.path.exists(pspath)):
        print("(2/4) Loading ProtonScript  ..... [ "+G+"OK"+E+" ]")
    else:
        print("(2/4) Loading ProtonScript ..... [ "+R+"FAIL"+E+" ]\n")
        import sys
        sys.exit()
    
    print("(3/4) Decoding Program File ..... [ "+G+"OK"+E+" ]")
    time.sleep(2)
    decoder(args.decode)
    print("(4/4) Saving Program File   ..... [ "+G+"OK"+E+" ]")
    time.sleep(2)
    print("")
    import sys
    sys.exit()
