import os,hashlib
dup_file={}
def compare(f1,f2):
	md1=hashlib.md5()
	md2=hashlib.md5()
	data1 = f1.read(2**20)
	data2 = f2.read(2**20)
	if not data1:
		return False
	if not data2:
		return False
	md1.update(data1)
	hex1=md1.hexdigest()
	md2.update(data2)
	hex2=md2.hexdigest()
	if hex1 == hex2:
		return True
	return False

def walk(path,ext,files=[]):
	global dup_file
	for name in os.listdir(path):
			if os.path.isdir(os.path.join(path, name)):
				walk(os.path.join(path, name),ext,files)
			elif os.path.isfile(os.path.join(path, name)) and os.path.exists(os.path.join(path,name)):
				if os.path.splitext(name)[1] == ext:
					for file in files:
						if name != file:
							f1 = open(file, 'rb')
							f2 = open(os.path.join(path,name),'rb')
							if compare(f1,f2):
								if file in dup_file:
									dup_file[file].append(os.path.join(path,name))
								else:
									dup_file[file]=[(os.path.join(path,name))]
walk('/home','.mp3',['s10.mp3','s21.mp3','s30.mp3'])
for key in dup_file:
	print('The Duplicate files for file ::',key)
	i=0
	for item in dup_file[key]:
		print(str(i)+'.--',item)
		i+=1
#tried with diff also but it was printing a lot of output so removed the command
