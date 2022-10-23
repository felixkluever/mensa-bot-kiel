import discord
import os
import oldScript
from dotenv import load_dotenv

load_dotenv()

KEY = os.getenv("DISCORD_KEY")

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

client.run(KEY)
