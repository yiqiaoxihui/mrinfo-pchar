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

#desc:
#获取边上的带宽
#当同一跳为不同的路由器ip时，取最后一个



def extract_pchar(file,result_file):
	nl=['0','1','2','3','4','5','6','7','8','9']
	all_ip=0
	host_distribution={}
	router_distribution={}
	bw_dic={}
	host_ip=0
	ip=0
	print file
	fr=open(file,'r')
	while True:
		line=fr.readline()
		if not line:
			break
		if ":" in line and len(line.split(":")[0])<=2:
			hop=int(line.split(":")[0])
			prev_hop=hop
			ip=line.split()[1]
			prev_ip=ip
			line=fr.readline()
			# while line.split()[1]==ip:
			# 	line=fr.readline()
			break
	no_flag=0
	while True:
		line=fr.readline()
		if not line:
			break
		if ":" in line and len(line.split(":")[0])<=2:	#ip in this line
			if "no probe responses" in line:		#no probe responses,
				no_flag=1
			else:
				no_flag=0
			prev_hop=hop
			prev_ip=ip
			hop=int(line.split(":")[0])
			ip=line.split()[1]
			line=fr.readline()
			#print line
			if len(line.split())<=1:	
				print ">>",line
		if "Hop char:" in line and no_flag==0:	#bw in this line,and have probe responses
			bw=line.split()[8]	#Kbps
			if bw=="0.000000" or "-" in bw or prev_ip=="no":
				continue
			if prev_hop+1==hop:			#必须是相邻的两跳
				key=prev_ip+","+ip
				print key, bw
				bw_dic[key]={}
				bw_dic[key]['bw']=bw

	fw=open(result_file,'w')
	for key in bw_dic:
		fw.write(key+","+bw_dic[key]['bw']+"\n")
	fw.close()
	print len(bw_dic)
if __name__=="__main__":
	path=sys.argv[1]
	file=sys.argv[2]
	extract_pchar(path,file)

