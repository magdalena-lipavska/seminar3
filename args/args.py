#!/usr/bin/env python3

import sys
import argparse

def cmdline_args():

    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpformatter)

    p.add_argument("argument", help="popis argumentu")
    p.add_argument("cislo", type=int, help="popis cisla")
    p.add_argument("-t", "--test", action="store_true", help="prepinac")
    p.add_argument("-x", help="ulozit")


    return p.parse_args()

if __name__ == '__main__':
    if sys.version_info < (3, 5, 0):
        sys.stderr.write('You need python 3.5 od later.\n')
        sys.exit(1)
    
    try:
        args = cmdline_args()
        print(args)
    except:
        print('Try args.py parametr -t')

        print()