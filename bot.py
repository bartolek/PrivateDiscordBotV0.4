import discord
from discord.ext import commands 
import helptxt

client = commands.Bot(command_prefix="$")

# Powiadomienie o poprawnym uruchomieniu bota
@client.event
async def on_ready():
    print("Bot uruchomił się poprawnie.")

# Odwołanie do pliku helptxt.py i egzekucja
client.remove_command("help")
@client.command()
async def help(ctx):
    await helptxt.help(ctx)


client.run("OTM3MDg4NTQ5NDQ1MDYyNzQ3.YfWpuA.87Lo-nPE0dKYyTGN7S6V4W58YU0")