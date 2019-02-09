import string
dic=dict()
great_dic={}
all_dic={}
all_list=[]
def word_histogram(word):
	global dic,all_dic
	dic[word]=dic.get(word,0)+1
	all_dic[word]=all_dic.get(word,0)+1

def depunctuate(line):
	for repl in string.punctuation:
		line=line.replace(repl, " ")
	return line

def compare_books(*books):
	global great_dic,dic
	for book in books:
		fout=open(book,'r')
		for line in fout:
			line=line.strip(string.whitespace+string.punctuation)
			line=depunctuate(line)
			for word in line.split():
				word_histogram(word)
		print('The Book Name is::',book)
		print('The Number of words in '+book+' Book::',sum(dic.values()))
		print('The Number of unique words in '+book+' Book::',len(dic))
		if len(great_dic)<len(dic):
			great_book=book
			great_dic,dic=dic,great_dic
		dic={}
	return great_book,great_dic

great_book,great_dic=compare_books('cobb.txt','new_year.txt','Precious_name.txt')
print("THE BOOK WITH GREATEST VOCABULARY IS::",great_book)
print("The Number of words in Book::",sum(great_dic.values()))
print("The Number of unique words in Book::",len(great_dic))
i=0
for item in sorted({(value,key)  for key,value in all_dic.items()},reverse=True):
	if i==20:
		break
	else:
		print('The word:: "',item[1],'" The Frequency::',item[0])
		i+=1
