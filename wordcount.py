#!/usr/local/env python

import os
import collections

db = {}
path = os.path.join(os.getcwd(),'word.txt')
print path
def wordcount(path):
	with open(path,'r') as f:
		f_all = f.read()
		f_all = f_all.lower()
		for word in  f_all.split():
			if word not in db:
				db[word] = 0
			db[word] += 1
		return db	

def sorted_by_db(d):
	d = collections.OrderedDict(sorted(d.items(), key = lambda t: -t[1]))

if __name__ == '__main__':
	print len(wordcount(path))
