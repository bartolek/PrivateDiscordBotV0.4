from unicodedata import name
import discord
from discord.ext import commands 
import helptxt
import random

intents = discord.Intents.default()
intents.members = True
intents.messages = True

client = commands.Bot(command_prefix="$", intents=intents)

# Powiadomienie o poprawnym uruchomieniu bota
@client.event
async def on_ready():
    print("Bot uruchomił się poprawnie.")
    await client.change_presence(activity=discord.Game(name="$help"))

# Odwołanie do pliku helptxt.py i egzekucja
client.remove_command("help")
@client.command()
async def help(ctx):
    await helptxt.help(ctx)

# Zmiana statusu bota Gra/Słucha
@client.command()
async def play(ctx, gamename):
    await client.change_presence(activity=discord.Game(name=gamename))

@client.command()
async def listen(ctx, songname):
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=songname))

#Losuj liczbe w przedziale
@client.command()
async def randomizer(ctx, min : int, max : int):
    if min < max:
        numer = random.randrange(min, max)
        await ctx.channel.send(numer)
    else:
        await ctx.channel.send("Pierwsza podana liczba musi być mniejsza od drugiej!")

currentStatus = "ON"

@client.command()
async def goomba(ctx, input : str):
    global currentStatus
    if input == "status":
        await ctx.channel.send(f"Aktualny status goomby to: {currentStatus}")    
    elif input == "ON" or input == "OFF":
        currentStatus = input
        await ctx.channel.send(f"Zmieniłeś status goomby na: {currentStatus}")
    else:
        await ctx.channel.send("Poprawne użycie komendy to: $goomba status/ON/OFF")

    

@client.listen('on_message')
async def on_messages(message):
    if message.attachments:
        if currentStatus == "ON":
            emojiA = '\U0001F1E6'
            emojiB = '\U0001F1E7'
            emojiC = '\U0001F1E8'
            emojiD = '\U0001F1E9'
            await message.add_reaction(emojiA)
            await message.add_reaction(emojiB)
            await message.add_reaction(emojiC)
            await message.add_reaction(emojiD)
            await client.process_commands(message)

    




#lista aktualnych komend
#help
#play nazwagry
#listen nazwapiosenki
#randomizer min max
#goomba status/on/off

client.run("OTM3MDg4NTQ5NDQ1MDYyNzQ3.YfWpuA.87Lo-nPE0dKYyTGN7S6V4W58YU0")