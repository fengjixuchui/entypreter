import argparse
import time
import os
    
def decoder(pscode):
    binary = open(pscode).read().split(" ")
    out = open(pscode[:pscode.index(".")] + ".p", "w")
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
    print("ProtonScript Coder 3.0\n")
    time.sleep(1)
    import os
    import os.path
    if (os.path.exists(args.run)):
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
    
    print("(3/4) Running Program File  ..... [ OK ]")
    time.sleep(2)
    print("")
    decoder(args.run)
