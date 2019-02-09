import string
fout=open('words.txt','r')
for line in fout:
	line=line.strip(string.whitespace+string.punctuation)
	print(line.split()[0])


