#!/bin/env python
import sys, getopt, re

def convert(x, f):
    return ({
        'd': lambda x: int(x),
        'b': lambda x: bin(x),
        'h': lambda x: hex(x),
        'o': lambda x: re.sub('o', '',oct(x))
    }[f](x))
help = lambda: print('ipconverter.py ip [format]\nFormat: d,b,h or o\n ex: ./ipconverter.py 127.0.0.1 o.h => 0177.0x1')
if(len(sys.argv)!=3 and len(sys.argv)!=2):
    help()
    sys.exit(2)
try:
    ip = list(map(int,sys.argv[1].split('.')))
    format= sys.argv[2].split('.') if len(sys.argv) == 3 else 'd'
    convertedIp=ip[:]
    convertedIp[len(format)-1]=0
    for i in range(5-len(format)):
        convertedIp[len(format)-1]+=ip[3-i]*pow(256,i)
    ret=""
    for i in range(len(format)):
        ret+='.' if i != 0 else ''
        ret+=str(convert(convertedIp[i],format[i]))
    print(ret)
except Exception as err:
    if type(err) == KeyError:
        print("Format error")
    else:
        print("There was an error")
    help()
    sys.exit(2)