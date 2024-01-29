import discord
import os
import oldScript
import scraper
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

KEY = os.getenv("DISCORD_KEY")

GITHUB_LINK = "github: https://github.com/felixkluever/mensa-bot-kiel"

def main():

    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'logged in as {client.user}')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('$plan'):
            await message.channel.send(embed=printWeek())

        if message.content.startswith("$montag"):
            await message.channel.send(embed=printDay(0))

        if message.content.startswith("$dienstag"):
            await message.channel.send(embed=printDay(1))

        if message.content.startswith("$mittwoch"):
            await message.channel.send(embed=printDay(2))

        if message.content.startswith("$donnerstag"):
            await message.channel.send(embed=printDay(3))

        if message.content.startswith("$freitag"):
            await message.channel.send(embed=printDay(4))

        if message.content.startswith("$heute"):
            await message.channel.send(embed=printToday())

    client.run(KEY)

def printDay(day: int):
    plan = scraper.getPlan()
    message = discord.Embed(
        title= intToDay(day) + " " + plan[day].date,
        url="https://studentenwerk.sh/de/mensaplandruck?ort=1&mensa=5"
    )
    message.set_footer(text=GITHUB_LINK)

    for item in plan[day].menu:
        message.add_field(
            name= item.name,
            value= item.price
        )

    return message

def printWeek():
    plan = scraper.getPlan()
    message = discord.Embed(
        title="Plan für die aktuelle Woche",
        url="https://studentenwerk.sh/de/mensaplandruck?ort=1&mensa=5"
    )
    message.set_footer(text=GITHUB_LINK)

    #if plan.__len__() < 5: #future code to handle weeks with a holiday
        
    if plan.__len__() > 0:
        for i, day in enumerate(plan):
            message.add_field(
                name= " - " + intToDay(i) + " - ",
                value=day.date,
                inline=False
            )
            for item in day.menu:
                val = ""
                if (item == day.menu[-1]):
                    val = item.price + "\n\nㅤ"
                else:
                    val = item.price
                message.add_field(
                    name= item.name,
                    value= val
                )
    else:
        message.add_field(
            name= "Die Mensa hat diese Woche geschlossen",
            value= " "
        )

    return message

def printToday():
    day = datetime.now().weekday()
    if (day <= 4):
        return printDay(day)
    else:
        message = discord.Embed(
            title= "Die Mensa ist am Wochenende geschlossen",
            url="https://studentenwerk.sh/de/mensaplandruck?ort=1&mensa=5",
            description="Die Schwentine Mensa ist am Wochenende geschlossen"
        )
        message.set_footer(text=GITHUB_LINK)
        return message

def intToDay(day:int) -> str:
    if (day == 0):
        return "Montag"
    elif (day == 1):
        return "Dienstag"
    elif (day == 2):
        return "Mittwoch"
    elif (day == 3):
        return "Donnerstag"
    elif (day == 4):
        return "Freitag"
    elif (day == 5):
        return "Samstag"
    elif (day == 6):
        return "Sonntag"

if (__name__ == "__main__"):
    main()