import discord
import asyncio
import logging
import os
import sys
import urllib.request
import json
from discord.ext import commands

#token handler
with open("..\\..\\tokens.json") as f:
	tokens = json.load(f)
	f.close()

TOKEN = tokens["tokens"]["bot-token"]
client = discord.Client()

bot = commands.Bot(command_prefix="!")

@client.event
async def papagoRequest(message, client, args):
	client_id =  tokens["tokens"]["papago-id"]
	client_secret = tokens["tokens"]["papago-token"]
	languages = {'en', 'ko', 'zn-CH', 'zn-TW', 'ja', 'es', 'fr', 'vi', 'th', 'id', 'ge'}
	dataIn = message.content()
	splitData = dataIn.split(" ")
	if splitData[1] not in languages and splitData[2] not in languages:
		return "Incorrect input or output language.".format(message)
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
		responseMsg = responseJson['message']['result']['translatedText'].format(message)
		return responseMsg
	else:
		return 'Papago Request Failed.'.format(message)

@client.event
async def test(message):
	msg = 'Hello {0.author.mention}'.format(message)
	await client.send_message(message.channel, msg)

@client.event
async def konlpy(message, client, args):
	msg = 'konlpy test **콜엔피우아이** {0.author.mention}'.format(message)
	await client.send_message(message.channel, msg)
ch.add_command({
	'trigger': "!konlpy",
	'function': konlpy,
	'args_num': 0, #need at least one thing to translate
	'args_name': [],
	'description': "starts the nlp processor for konlpy"
})	
@client.event
async def kill(message, client, args):
	await client.logout()
	return "Kill me".format(message)
ch.add_command({
	'trigger': "!kill",
	'function': kill,
	'args_num': 0, #need at least one thing to translate
	'args_name': [],
	'description': "this kills the bot"
})	
#main method of bot
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
	if message.author == client.user:
		return
	else:
		# try to evaluate with the command handler
		try:
			bot.process_commands(message)
		# message doesn't contain a command trigger
		except TypeError as e:
			pass
		# generic python error
		except Exception as e:
			print(e)
			
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)