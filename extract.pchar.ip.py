
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
#usage :  python extract.char.ip edge_file target_file
def extract_pchar_ip(file_dir,result_file):
	all_ip=0
	rset=set()
	host_ip=0
	fr=open(file_dir,'r')
	while True:
		line=fr.readline()
		if not line:
			break
		else:
			l=line.strip().split(",")
			#print l[1],1[0]
			ip_begin=socket.ntohl(struct.unpack("I",socket.inet_aton(l[1]))[0])
			ip_end=socket.ntohl(struct.unpack("I",socket.inet_aton(l[0]))[0])
			rset.add(l[1]+","+str(ip_begin))
			rset.add(l[0]+","+str(ip_end))

	fr.close()
	fw=open(result_file,'w')
	for pair in rset:
		fw.write(pair+"\n")
	fw.close()
	print len(rset)
if __name__=="__main__":
	path=sys.argv[1]
	file=sys.argv[2]
	extract_pchar_ip(path,file)

