from unicodedata import name
from black import err
import discord, json
from discord.ext import commands 
import os
import sqlite3


intents = discord.Intents.default()
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix="$", intents=intents)

# Powiadomienie o poprawnym uruchomieniu bota
@bot.event
async def on_ready():
    print("Bot uruchomił się poprawnie.")
    await bot.change_presence(activity=discord.Game(name="$help"))
    db = sqlite3.connect("discord.db")
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS info(guild_id INT, text STR)")
    cursor.close()
    db.close()

bot.remove_command("help")

for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")


#Error Handling

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Taka komenda nie istnieje")

with open("key.json","r") as key:
    data = json.load(key)
    bot.run(data.get("key"))