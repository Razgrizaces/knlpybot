from konlpy.tag import Kkma
from konlpy.utils import pprint
import io
import pandas

#algo:
#nlp to levels using pandas
#parse using kkma function that takes input text into words
#after parse, output one sentence per analyzed word 
#order of sentence:
#word - nlp type: example | sentence example with bold (discord is **** for bold)
#(bonus if in order, but if not then we'll fix or try to)

#extras: naver lookup to find the meaning
#sentence builder with particles or number of things

kkma=Kkma()
filename = "konlpytest.csv"
sentence = '아 진짜요? 오늘 너무 힘들은거 같아요... 수고했어요~'
i = 0
#create the csv
with io.open(filename, "w", encoding = "utf8") as f:
	while i is not len(kkma.sentences(sentence)):
		#tuple check
		f.write(',\n'.join('%s, %s' % x for x in kkma.pos(kkma.sentences(sentence)[i])))
		f.write(',\n')
		i = i+1
#csv created

