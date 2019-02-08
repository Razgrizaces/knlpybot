from konlpy.tag import Okt
from konlpy.tag import Kkma
from konlpy.utils import pprint
import tossi 		
import io		
import pandas as pd

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
okt=Okt()
print("Done loading!")
#invalidTags = {"SF", "SE", "SS", "SP", "SO", "SW"}
sentence = '안녀하세요, 저는 트리스예요 ㅋㅋㅋㅋㅋ 저는 뉴욕에 살아요. 만나서 반사습니다~'
filename = "..\\csvs\\konlpytest.csv"
invalidTags = {"Unknown", "Number","Foreign", "Alpha", "Hashtag","ScreenName", "Email", "URL", "Punctuation"}
i = 0
#create the csv
with io.open(filename, "w", encoding = "utf8") as f:
	#while i is not len(kkma.sentences(sentence)):
	#	#tuple check
	#	j = 0
	#	while j is not len(kkma.pos(kkma.sentences(sentence)[i])):
	#		if kkma.pos(kkma.sentences(sentence)[i])[j][1] not in invalidTags:
	#			f.write(kkma.pos(kkma.sentences(sentence)[i])[j][0])
	#			f.write(",")
	#			f.write(kkma.pos(kkma.sentences(sentence)[i])[j][1])
	#			f.write("\n")
	#		j = j+1
	#	i = i + 1
	#while i is not len(okt.sentences(sentence)):
		#tuple check
		#j = 0
	while i is not len(okt.pos(sentence)):
		if okt.pos(sentence)[i][0] not in invalidTags:
			f.write(okt.pos(sentence)[i][0])
			f.write(",")
			f.write(okt.pos(sentence)[i][1])
			f.write("\n")
		i = i + 1	
	f.close()
#csv created

#cols = ["pos","korean","T1 Class KR","T1 Class English","T3 Korean","T3 English","sentence examples"]
cols = ["pos","korean1"]
posCols = ["pos", "korean"]

#create data frame from cols with nlp_to_level
#nlpDf = pd.read_csv("..\\csvs\\nlp_to_level.csv", names = cols)
nlpDf = pd.read_csv("..\\csvs\\twt_to_level.csv", names = cols)
#create df using posCols with file from before
posDf = pd.read_csv(filename, names= posCols)

#merge the dfs
print(nlpDf)
print(posDf)
posDf.to_csv("testdf.csv")
posDf = posDf.merge(nlpDf, on = ["pos"])
print(posDf)
#posDf.to_csv("testdf.csv")