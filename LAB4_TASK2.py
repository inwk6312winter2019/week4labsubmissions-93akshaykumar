import string
dic=dict()
great_dic={}
def word_histogram(word):
	global dic
	dic[word]=dic.get(word,0)+1

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

