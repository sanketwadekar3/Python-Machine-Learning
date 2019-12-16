import sys
import os
import hashlib

def hashfile(path, blocksize = 1024):
	afile = open(path,'rb')
	hasher = hashlib.md5()
	buf = afile.read(blocksize)
	while len(buf)>0:
		hasher.update(buf)
		buf = afile.read(blocksize)
	afile.close()
	return hasher.hexdigest()

def DisplayChecksum(path):
	line = "-"*40
	flag = os.path.isabs(path)
	if flag == False:
		path = os.path.abspath(path)
		
	exists = os.path.isdir(path)
	
	if exists:
		for dirName, subdirs, fileList in os.walk(path):
			print("Current folder is: "+dirName)
			for filen in fileList:
				path = os.path.join(dirName, filen)
				file_hash = hashfile(path)
				print(line)
				print(path)
				print(file_hash)
	
def main():
	DisplayChecksum(sys.argv[1])
	
if __name__ == '__main__':
	main()