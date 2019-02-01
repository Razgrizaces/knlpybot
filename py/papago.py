import os
import sys
import urllib.request
import json

with open("..\\..\\tokens.json") as f:
	data = json.load(f)
	f.close()
client_id =  data["tokens"]["papago-id"]
client_secret = data["tokens"]["papago-token"]
encText = urllib.parse.quote("Hi, I'm Tris.")
inLang = -1
outLang = -1

languages = {'en', 'ko', 'zn-CH', 'zn-TW', 'ja', 'es', 'fr', 'vi', 'th', 'id', 'ge'}
dataIn = input("usage: !translate inLang outLang message\n")
splitData = dataIn.split(" ")
if splitData[1] not in languages and splitData[2] not in languages:
	print("Incorrect input or output language.")
inLang = splitData[1]
outLang = splitData[2]
#get message part
encText = " ".join(splitData[3:])
data = "source=" + inLang + "&target="+ outLang + "&text=" + encText
print(data)
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
	response_body = response.read()
	responseJson = json.loads(response_body.decode('utf-8'))
	with open("testTranslation.txt", "w", encoding = "utf-8") as f:
		f.write(responseJson['message']['result']['translatedText'])
		f.close()
	
else:
    print("Error Code:" + rescode)