#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys


def checkExists(file_path):
	if os.path.exists(file_path):
		return True
	else:
		return False

def putFile(file_path, files):
	if os.path.isdir(file_path):
		for i in os.listdir(file_path):
			if i.split('.')[1] == 'mp3':
				files.append("%s/%s"%(file_path, i))
	elif file_path.split('.')[1] == 'mp3':
		files.append(file_path)


def converOgg(files):
	for file in files:
		try:
			out_path = file.split('.')[0] + '.ogg'
			os.system("mpg321 %s -w raw && oggenc raw -o %s && rm raw"%(file, out_path))
		except Exception as e:
			print(str(e))


if __name__ == '__main__':
	argv = sys.argv
	files = []
	if not checkExists(argv[1]):
		sys.exit()
	else:
		putFile(argv[1], files)
		converOgg(files)
		print('[SUCCESS] think you for you use')


