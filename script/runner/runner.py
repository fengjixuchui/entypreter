import argparse
import time
import os

G = "\033[1m"
R = "\033[1m"
E = "\033[0m"
    
def decoder(pscode):
    binary = open(pscode).read()
    out = open(pscode[:pscode.index(".")] + ".p", "w")
    if binary == '':
        out.write('')
        return None
    binary = binary.split(" ")
    text = ""
    for i in binary:
        text += chr(int(i, base=2))
    out.write(text)
    out.close()
    
parser = argparse.ArgumentParser()
parser.add_argument("-r","--run", metavar='FILE', help="Run a ProtonScript program file.")
args = parser.parse_args()

if args.run:
    argrem = args.run
    time.sleep(1)
    import os
    import os.path
    if (os.path.exists(args.run)):
        if '.' in args.run:
            time.sleep(0)
        else:
            print("\n(1/3) Loading Program File ..... [ "+R+"FAIL"+E+" ]\n")
            import sys
            sys.exit()
            
        if (argrem[-(argrem[::-1].index('.')):]) == 'psc':
            print("\n(1/3) Loading Program File  ..... [ "+G+"OK"+E+" ]")
            
        else:
            print("\n(1/3) Loading Program File ..... [ "+R+"FAIL"+E+" ]\n")
            import sys
            sys.exit()
    else:
        print("\n(1/3) Loading Program File ..... [ "+R+"FAIL"+E+" ]\n")
        import sys
        sys.exit()
        
    if (os.path.exists("/data/data/com.termux")):
        pspath = "/data/data/com.termux/files/usr/bin/pscript"
    else:
        pspath = "/usr/local/bin/pscript"
        
    time.sleep(1)
            
    if (os.path.exists(pspath)):
        print("(2/3) Loading ProtonScript  ..... [ "+G+"OK"+E+" ]")
    else:
        print("(2/3) Loading ProtonScript ..... [ "+R+"FAIL"+E+" ]\n")
        import sys
        sys.exit()
    
    print("(3/3) Running Program File  ..... [ "+G+"OK"+E+" ]")
    time.sleep(2)
    decoder(args.run)
