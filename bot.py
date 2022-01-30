from unicodedata import name
import discord
from discord.ext import commands 
import helptxt
import random

client = commands.Bot(command_prefix="$")

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
    



#lista aktualnych komend
#help
#play nazwagry
#listen nazwapiosenki
#randomizer min max

client.run("OTM3MDg4NTQ5NDQ1MDYyNzQ3.YfWpuA.87Lo-nPE0dKYyTGN7S6V4W58YU0")