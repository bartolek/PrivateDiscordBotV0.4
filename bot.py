from unicodedata import name
from black import err
import discord
from discord.ext import commands 
import helptxt
import random
import requests 


intents = discord.Intents.default()
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix="$", intents=intents)

# Powiadomienie o poprawnym uruchomieniu bota
@bot.event
async def on_ready():
    print("Bot uruchomił się poprawnie.")
    await bot.change_presence(activity=discord.Game(name="$help"))

# Odwołanie do pliku helptxt.py i egzekucja
bot.remove_command("help")
@bot.command()
async def help(ctx):
    await helptxt.help(ctx)

# Zmiana statusu bota Gra/Słucha
@bot.command()
async def play(ctx, gamename):
    await bot.change_presence(activity=discord.Game(name=gamename))

@bot.command()
async def listen(ctx, songname):
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=songname))

#Losuj liczbe w przedziale
@bot.command()
async def randomizer(ctx, min : int, max : int):
    if min < max:
        numer = random.randrange(min, max)
        await ctx.channel.send(numer)
    else:
        await ctx.channel.send("Pierwsza podana liczba musi być mniejsza od drugiej!")

#Goomba
currentStatus = "OFF"

@bot.command()
async def goomba(ctx, input : str):
        global currentStatus
        if input == "status":
            await ctx.channel.send(f"Aktualny status goomby to: {currentStatus}")    
        elif input == "ON" or input == "OFF":
            currentStatus = input
            await ctx.channel.send(f"Zmieniłeś status goomby na: {currentStatus}")
        else:
            await ctx.channel.send("Poprawne użycie komendy to: $goomba status/ON/OFF")

@bot.listen('on_message')
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
            await bot.process_commands(message)

#Wilusz reaction emoji
@bot.listen('on_message')
async def Wilusz(message):
    słownik = ['Wilusz', 'wilusz', 'Wilusza', "wilusza"]
    for word in słownik:
        if word in message.content:
            await message.add_reaction('\U00002642')

#Error Handling

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Taka komenda nie istnieje")

@goomba.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("W komendzie brakuje argumentu")

@randomizer.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("Poprawne użycie komendy to: $randomizer int int")

@bot.command()
async def kanyenadzis(ctx):
    response = requests.get("https://api.kanye.rest")
    api = response.json()
    await ctx.send(api.get('quote'))




#lista aktualnych komend
#help
#play nazwagry
#listen nazwapiosenki
#randomizer min max
#goomba status/on/off
#kanyenadzis

bot.run("OTM3MDg4NTQ5NDQ1MDYyNzQ3.YfWpuA.87Lo-nPE0dKYyTGN7S6V4W58YU0")