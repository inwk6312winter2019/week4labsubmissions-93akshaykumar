import os

listfile=[]
listdir=[]

def walk(path):
	global listfile,listdir
	for name in os.listdir(path):
		if os.path.isdir(os.path.join(path, name)):
			listdir.append(name)
			walk(os.path.join(path, name))
		elif os.path.isfile(os.path.join(path, name)):
			listfile.append(name)
#walk('/home/akshaykumar')
print('The files present in home')
#readfile('/home/akshaykumar/akshaykumar')
walk('/home')
print('THE LIST OF ALL THE FILES IN HOME AND SUB FOLDERS')
for item in listfile:
	print(listfile,sep="***",end="")
print()
print('THE LIST OF ALL THE DIRECTORIES IN HOME AND SUB DIRECTORIES IN REVERSE')
for item in listdir:
	print(item[::-1])
#print(os.listdir('/home'))
