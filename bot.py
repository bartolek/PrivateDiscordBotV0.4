from unicodedata import name
from black import err
import discord
from discord.ext import commands 
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

bot.remove_command("help")

for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")

#Error Handling

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Taka komenda nie istnieje")

bot.run("OTM3MDg4NTQ5NDQ1MDYyNzQ3.YfWpuA.87Lo-nPE0dKYyTGN7S6V4W58YU0")