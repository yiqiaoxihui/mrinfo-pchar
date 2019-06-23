
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
import json
import time
import math
import socket
import hashlib
import struct
def extract_mrinfo_ip(file_dir,result_file):
	all_ip=0
	host_distribution={}
	router_distribution={}
	rset=set()
	host_ip=0
	list_dir = os.listdir(file_dir)
	
	for file in list_dir:
		if (file[-2:]==".r"):
			print file
			fr=open(file,'r')
			while True:
				line=fr.readline()
				if not line:
					break
				if "->" in line:
					l=line.strip().split()
					if len(l)<3:
						continue
					#print l[0],l[2]
					ip_begin=socket.ntohl(struct.unpack("I",socket.inet_aton(str(l[0])))[0])
					ip_end=socket.ntohl(struct.unpack("I",socket.inet_aton(str(l[2])))[0])
					if ip_begin==0 or ip_end==0:
						continue
					if ip_begin==ip_end:
						continue
					if l[0][0:3]=="10." or l[2][0:3]=="10.":
						continue
					rset.add(l[2])
					rset.add(l[0])

			fr.close()
	fw=open(result_file,'w')
	for pair in rset:
		fw.write(pair+"\n")
	fw.close()
	print len(rset)
if __name__=="__main__":
	path=sys.argv[1]
	file=sys.argv[2]
	extract_mrinfo_ip(path,file)


