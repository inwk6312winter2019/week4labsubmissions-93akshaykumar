import string
import matplotlib.pyplot as pyplot
import math
from operator import itemgetter
book_list=[]
book_dic={}
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

book_list=[(values,keys) for keys,values in sorted(book_dic.items())]
book_list=sorted(book_list,reverse=True)
#print(book_list)
pyplot.clf()
pyplot.xscale('log')
pyplot.yscale('log')
pyplot.title('The Zipf graph')
pyplot.xlabel('Rank')
pyplot.ylabel('frequency')
for rank in range(2,len(book_list)):
	#pyplot.plot(math.log(rank),math.log(book_list[rank-2][0]))
	pyplot.plot(rank,rank)
pyplot.show()

