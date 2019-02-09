def sed_that(pat_str,arg_str,file1,file2):
	try:
		fout=open(file1,'r')
		fin=open(file2,'a')
		for line in fout:
			line=line.replace(pat_str,arg_str)
			fin.write(line)
		fout.close()
		fin.close()
	except:
		print('Error Occured while performing File Error')

sed_that('the','eht','cobb.txt','tempcreate.txt')
print('The file write Done')
