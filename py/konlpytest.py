from konlpy.tag import Kkma
from konlpy.tag import Mecab
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
print("Done loading!")
filename = "..\\csvs\\konlpytest.csv"
sentence = '발표 무사히 끝냈어요! 주말에 빈 회의실 가서 혼자 연습했어요 ㅠㅠ 청중역으로 인형 갖다두고 그거 보면서 연습하고 발표할때도 저건 사람이 아니라 인형이다 이러고 했습니다 ㅠㅠ'
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
				f.write(",")
				f.write(kkma.pos(kkma.sentences(sentence)[i])[j][1])
				f.write("\n")
			j = j+1
		i = i + 1
	f.close()
#csv created

cols = ["pos","korean","T1 Class KR","T1 Class English","T3 Korean","T3 English","sentence examples"]
posCols = ["word", "pos"]

#create data frame from cols with nlp_to_level
nlpDf = pd.read_csv("..\\csvs\\nlp_to_level.csv", names = cols)
#create df using posCols with file from before
posDf = pd.read_csv(filename, names= posCols)

#merge the dfs
print(nlpDf)
posDf = posDf.merge(nlpDf, on = ["pos"])
posDf.to_csv("testdf.csv")