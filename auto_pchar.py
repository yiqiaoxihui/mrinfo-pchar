import os
import sys
import shlex
import subprocess
import time
file_path=sys.argv[1]
print  file_path

fw_result=open(sys.argv[2],'w')
fr=open(file_path,'r')
while True:
	ip=fr.readline()
	if not ip:
		break
	else:
		ip=ip.strip()
		cmd="./pchar -n -I 400 -R 3 -t 2 -p ipv4icmp "+ip
		print cmd
		cmd = shlex.split(cmd)
		p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		while p.poll() is None:
			line = p.stdout.readline()
			fw_result.write(line)
			print line.strip()
fw_result.close()