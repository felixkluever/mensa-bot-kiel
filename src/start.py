import discord
import oldScript

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$plan'):
        await message.channel.send(oldScript.getPlan())

client.run('MTAzMzgxNDA5MzM2NDIxOTk2NQ.GCp0p2.WYMWaA0LNZVK6DSumJG2TwL5DQVXu4HX9MkG7c')
