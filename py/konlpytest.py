from konlpy.tag import Kkma
from konlpy.utils import pprint
import io
import pandas

#algo:
#nlp to levels with csv (O)
#using pandas 
#parse using kkma function that takes input text into words (O)
#after parse, output one sentence per analyzed word 
#order of sentence:
#word - nlp type: example | sentence example with bold (discord is ** text ** for bold)
#(bonus if in order, but if not then we'll fix or try to)

#extras: naver lookup to find the meaning
#sentence builder with particles or number of things

print("Loading KKMA...")
kkma=Kkma()
print("Done loading!")
filename = "konlpytest.csv"
sentence = '아 진짜요? 오늘 너무 힘들은거 같아요... 수고했어요~'
invalidTags = {"SF", "SE", "SS", "SP", "SO", "SW"}
i = 0
#create the csv
with io.open(filename, "w", encoding = "utf8") as f:
	while i is not len(kkma.sentences(sentence)):
		#tuple check
		j = 0
		while j is not len(kkma.pos(kkma.sentences(sentence)[i])):
			if kkma.pos(kkma.sentences(sentence)[i])[j][1] not in invalidTags:
				f.write(kkma.pos(kkma.sentences(sentence)[i])[j][0])
				f.write(", ")
				f.write(kkma.pos(kkma.sentences(sentence)[i])[j][1])
				f.write(",\n")
			j = j+1
		i = i + 1
#csv created
#

cols = {"pos","korean","T1 Class KR","T1 Class English","T3 Korean","T3 English","sentence examples"}
posCols = {"word", "pos")

#create data frame from cols with nlp_to_level

#create df using posCols with 