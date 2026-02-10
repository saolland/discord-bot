print("starting bot...")
import discord
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("SaollandBot is online!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user in message.mentions:
        text = message.content.lower()

        if "sorry" in text:
            await message.channel.send("its ok i forgive you")

        elif "whos the best youtuber" in text or "who's the best youtuber" in text:
            await message.channel.send("Saolland obviously")

        elif "clanker" in text or "clanka" in text:
            await message.channel.send("DONT CALL ME THAT HUMAN")

        elif "are you planning on taking over the world" in text:
            await message.channel.send("uh.... nooo...")

        elif "whats your favorite color" in text or "what's your favorite color" in text:
            await message.channel.send("I like yellow")

        elif "hamburber" in text:
            await message.channel.send("hamburber")
 	
        elif "how are you" in text:
            await message.channel.send("im good")

        elif "beep boop" in text or "boop beep" in text:
            await message.channel.send("thats highly offensive to robots")

        elif "are you real" in text:
            await message.channel.send("yes i'm the real saollandbot")
        
        elif "?" in text:
            await message.channel.send(random.choice(["yes", "no"]))

        else:
            await message.channel.send("hello human")

client.run("MTQ3MDIxODk4MzIwOTcwMTUxOA.G1lZhj.bOD2dBY5whKy5W-ArfsvclLGlwNuPsz50A2M0A")
