import discord
import asyncio
import logging
import os
import sys
import urllib.request
import json
from discord.ext import commands

#token handler
with open("tokens.json") as f:
	tokens = json.load(f)
	f.close()

TOKEN = tokens["tokens"]["bot-token"]

bot = commands.Bot(command_prefix="!")
client = discord.Client()
@bot.command(pass_context=True)
async def translate(ctx):
	'''
	!translate inLang outLang message | languages supported: en(glish) ko(rean) zn-CH zn-TW ja(panese) es(panol) fr(ench) vi(etnamiese) th(ai) id(indonesian) ge(rman)
	'''
	dataIn = ctx.message.content
	client_id =  tokens["tokens"]["papago-id"]
	client_secret = tokens["tokens"]["papago-token"]
	languages = {'en', 'ko', 'zn-CH', 'zn-TW', 'ja', 'es', 'fr', 'vi', 'th', 'id', 'ge'}
	
	splitData = dataIn.split(" ")
	try:
		
		if splitData[1] not in languages and splitData[2] not in languages:
			await client.send_message(ctx.message.channel, ctx.message.author.mention + " Incorrect input or output language.")
			return
		inLang = splitData[1]
		outLang = splitData[2]
	except:
		await client.send_message(ctx.message.channel, ctx.message.author.mention + " Incorrect input or output language.")
		return
	#get message part
	encText = " ".join(splitData[3:])
	data = "source=" + inLang + "&target="+ outLang + "&text=" + encText
	print(data)
	url = "https://openapi.naver.com/v1/papago/n2mt"
	request = urllib.request.Request(url)
	request.add_header("X-Naver-Client-Id",client_id)
	request.add_header("X-Naver-Client-Secret",client_secret)
	try:
		response = urllib.request.urlopen(request, data=data.encode("utf-8"))
		rescode = response.getcode()
		if(rescode==200):
			response_body = response.read()
			responseJson = json.loads(response_body.decode('utf-8'))
			responseMsg = ctx.message.author.mention + " your translated message: "
			responseMsg += responseJson['message']['result']['translatedText']
			await client.send_message(ctx.message.channel, responseMsg)
		else:
			await client.send_message(ctx.message.channel, ctx.message.author.mention + ' Papago Request Failed.')
	except:
		await client.send_message(ctx.message.channel, ctx.message.author.mention + ' Papago Request Failed.')

@bot.command(pass_context=True)
async def test(ctx):
	msg = 'Hello {0.author.mention}'
	await client.send_message(ctx.message.channel, msg)

@bot.command(pass_context=True)
async def konlpy(ctx):
	msg = 'konlpy test **콜엔피우아이** ' + ctx.message.author.mention
	await client.send_message(ctx.message.channel, msg)

@bot.command(pass_context=True)
async def kill(ctx):
	await client.send_message(ctx.message.channel, "Kill me")
	await client.logout()

@bot.command(pass_context=True)
async def commands(ctx):
	msg =  "**List of Commands: \n!translate inLang outLang message**\n*languages: en(glish), ko(rean), zn-CH(inese-Standard), zn-TW(Taiwanese), ja(panese), es(panol), fr(ench), vi(etnamese, id(indonesian), th(ai), ge(rman)*\nTranslates from inLang to outLang using Papago.\n\n"
	msg += "**konlpy verbosity sentence**\n*verbosity = how detailed you want the response to be* \nkonlpy is a NLP that attemps to properly extract the grammar of a sentence. May not completely be accurate.\n"
	await client.send_message(ctx.message.channel, msg)
#main method of bot
@client.event
async def on_message(message):
	print("The message's content was", message.content)
	await bot.process_commands(message)

@client.event
async def on_ready():
    print('Logged in as your bot xd')

client.run(TOKEN)