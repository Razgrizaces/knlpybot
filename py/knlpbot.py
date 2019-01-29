import discord
import asyncio
import logging


TOKEN = 'NTM4MDQyNDg1MjE0MjgxNzQw.Dyy_dA.rtPj1GP_sKayM_3K3_3jR8magtI'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)