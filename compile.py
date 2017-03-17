#!/bin/bash

import re
import os
from fnmatch import fnmatch,fnmatchcase


line = 'asdf fjdk; afed, fjek,asdf, foo'
#
field = re.split(r'[,;\s]\s*',line)
print re.split(r'(;|,|\s)\s*', line)
values = field
print field
print field[::]
print re.split(r'(?:,|;|\s)\s*', line)

filename='file.txt'
print filename.endswith('.txt')
print filename.startswith('file')
url='http://172.27.4.9:8088'
print url.startswith('http:')

filename = os.listdir('.')
print [name for name in filename if name.endswith('.py')]

print any(name.endswith('.py') for name in filename)

print re.match(r'http|ftp',url)

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print [name for name in names if fnmatch(name,'Dat[0-9].csv')]


addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

print [addr for addr in addresses if fnmatchcase(addr,'* ST')]


txt1 = '11/27/2012'

if re.match(r'\d+/\d+/\d',txt1):
    print  'yes'
else:
    print 'no'


datapat = re.compile(r'\d+/\d+/\d+')
if datapat.match(txt1):
    print 'yes'
else:
    print 'no'

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print "---------------------------"
test = text.replace('PyCon','whwstar')
print test
print datapat.match(text)
print datapat.findall(text)


datapat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datapat.match(txt1)
print m
print m.group()
print m.group(1)
print m.group(2)
print m.group(3)
m = datapat.findall(text)
print m


for day,month,year in m:
    print('{0}-{1}-{2}'.format(year,month,day))

datapat = re.compile(r'(\d+)/(\d+)/(\d+)$')
m=datapat.match('12/23/2016')
print m.group()

print datapat.match('11/27/2012abcdef')

