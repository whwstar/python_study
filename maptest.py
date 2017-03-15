#!/bin/en python

#!/bin/env python

"""an example for Unicode insert file"""
CODEC = 'utf-8'
FILE = '/home/whwstar/unicode.txt'
hello_out = u"Hello world\n"
bytes_out = hello_out.encode(CODEC)
f = open(FILE,"w")
f.write(bytes_out)
f.close()

f = open(FILE,'r')
bytes_in=f.read()
aa = bytes_in.decode(CODEC)
print aa

