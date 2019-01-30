import discord
import asyncio
import logging
import os
import sys
import urllib.request

TOKEN = 'NTM4MDQyNDg1MjE0MjgxNzQw.Dyy_dA.rtPj1GP_sKayM_3K3_3jR8magtI'
client = discord.Client()

@client.event
async def papagoRequest(request, en, ko):
	client_id = "cNG69MHtiwvlRqbBHSJK"
	client_secret = "tTeMWZEjRT"
	encText = urllib.parse.quote("Hi, I'm Tris.")
	data = "source=" + "&target=_"+ "&text=" + encText
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

@client.event
async def parseArguments(args):
	str = args.split(" ")

@client.event
async def test(message):
	msg = 'Hello {0.author.mention}'.format(message)
	await client.send_message(message.channel, msg)

@client.event
async def konlpy(message):
	msg = 'konlpy test **콜엔피우아이** {0.author.mention}'.format(message)
	await client.send_message(message.channel, msg)

@client.event
async def kill(message):
	await client.logout()

	
#main method of bot
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
	if message.author == client.user:
		return
	if message.content.startswith('!'):
		options = {
			"hello": test(message),
			"konlp": konlpy(message),
			"stop": kill(message)
		}
		testmsg = message.content.split()
		testmsg = (testmsg[0][1:]).strip()
		#options.get(testmsg, "Invalid command.")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)