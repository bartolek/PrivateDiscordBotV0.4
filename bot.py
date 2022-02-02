from unicodedata import name
from black import err
import discord
from discord.ext import commands 
import requests 
import os


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

for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")


#Goomba
currentStatus = {'937667379159248946': 'OFF'
}

@bot.command()
async def goomba(ctx, input : str):
        global currentStatus
        channel_id = ctx.message.guild.id
        if input == "status":
            if str(channel_id) in currentStatus:
                await ctx.channel.send(f"Aktualny status goomby na tym serwerze to: {currentStatus.get(str(channel_id))}")
            else:
                currentStatus[str(channel_id)] = 'OFF'
                await ctx.channel.send(f"Aktualny status goomby na tym serwerze to: {currentStatus.get(str(channel_id))}")
        elif input == "ON" or input == "OFF":
            currentStatus[str(channel_id)] = input
            await ctx.channel.send(f"Zmieniłeś status goomby na tym serwerze na: {currentStatus.get(str(channel_id))}")
        else:
            await ctx.channel.send("Poprawne użycie komendy to: $goomba status/ON/OFF")

@bot.listen('on_message')
async def on_messages(message):
    if message.attachments:
        if currentStatus.get(str(message.guild.id)) == "ON":
            await message.add_reaction('\U0001F1E6')
            await message.add_reaction('\U0001F1E7')
            await message.add_reaction('\U0001F1E8')
            await message.add_reaction('\U0001F1E9')
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


#@goomba.error
#async def on_command_error(ctx, error):
#    if isinstance(error, commands.MissingRequiredArgument):
#        await ctx.send("W komendzie brakuje argumentu")


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