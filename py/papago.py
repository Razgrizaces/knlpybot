import os
import sys
import urllib.request
import json

with open("..\\..\\tokens.json") as f:
	data = json.load(f)

client_id =  data["tokens"]["papago-id"]
client_secret = data["tokens"]["papago-token"]
encText = urllib.parse.quote("Hi, I'm Tris.")
inLang = -1
outLang = -1
while not (inLang == 0 or inLang ==1):
	try:	
		inLang = int(input("Input data: type 0 for 한국어, type 1 for English.\n"))
	except ValueError:
		print("Please type either 1 or 0.\n")
		
while not (outLang == 0 or outLang == 1):
	try:	
		outLang = int(input("Output data: type 0 for 한국어, type 1 for English.\n"))
	except ValueError:
		print("Please type either 1 or 0.\n")
if (inLang == 0):
	inLang = "ko"
else:
	inLang = "en"
if (outLang == 0):
	outLang = "ko"
else:
	outLang = "en"
data = "source=" + inLang + "&target=_"+ outLang + "&text=" + encText
print(data)
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)