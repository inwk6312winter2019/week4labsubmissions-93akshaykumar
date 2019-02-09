import string
book_list=[]
book_dic={}
file_list=[]
file_dic={}
common_list=[]
noncommon_list=[]
def word_histogram(word):
	global dic


def depunctuate(line):
	for repl in string.punctuation:
		line=line.replace(repl, " ")
	return line
def read(file):
	dic={}
	fout=open(file,'r')
	for line in fout:
		line=line.strip(string.whitespace+string.punctuation)
		line=depunctuate(line)
		for word in line.split():
			dic[word]=dic.get(word,0)+1
	return dic

book_dic=read('cobb.txt')
file_dic=read('words.txt')
book_list=set(book_dic)
file_list=set(file_dic)
diff_dic=book_list.difference(file_list)
print('The Number of Words present in Book but not in word file::',diff_dic)
for vale in diff_dic:
	if book_dic[vale]>5:
		common_list.append(vale)
	else:
		noncommon_list.append(vale)

print('The list of Common words(occurance > 5):::')
print(common_list)

print('The list of NON Common words(occurance < 5):::')
print(noncommon_list)
