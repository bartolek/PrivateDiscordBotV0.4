from unicodedata import name
from black import err
import discord, json
from discord.ext import commands 
import os
import sqlite3
import time


intents = discord.Intents.default()
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix="$", intents=intents)

# Powiadomienie o poprawnym uruchomieniu bota oraz wpisywanie pytań użytkowników do bazy danych + stworzenie bazy warnów
@bot.event
async def on_ready():
    print("Bot uruchomił się poprawnie.")
    await bot.change_presence(activity=discord.Game(name="$help"))
    db = sqlite3.connect("discord.db")
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS info(guild_id INT, text STR, nickname STR)")
    cursor.execute("CREATE TABLE IF NOT EXISTS warns(guild_id INT, user_id INT, reason STR, author_id INT, date INT)")
    cursor.close()
    db.close()

@commands.cooldown(1, 1800, commands.BucketType.user)
@bot.command()
async def question(ctx, *, texts):
    db = sqlite3.connect("discord.db")
    cursor = db.cursor()
    cursor.execute("INSERT INTO info(guild_id, text, nickname) VALUES(?, ?, ?)", (ctx.author.guild.id, texts, ctx.message.author.name))
    cursor.close()
    db.commit()
    db.close()
    await ctx.send("Pytanie zostało zapisane w bazie danych.")

@bot.command()
async def questiondel(ctx):
    db = sqlite3.connect("discord.db")
    cursor = db.cursor()
    cursor.execute("DROP TABLE info")
    cursor.execute("CREATE TABLE info(guild_id INT, text STR, nickname STR)")
    cursor.close()
    db.commit()
    db.close()
    await ctx.send("Baza z pytaniami została usunięta.")

@bot.command()
async def questionshow(ctx):
    db = sqlite3.connect("discord.db")
    cursor = db.cursor()
    cursor.execute("SELECT text, nickname FROM info LIMIT 5")
    x = cursor.fetchall()
    for row in x:
        await ctx.send(f"Nick: {row[1]} \nPytanie: {row[0]}")
    cursor.close()
    db.commit()
    db.close()

#Warns
@bot.command()
async def warn(ctx, member: discord.Member, *,reason):
    db = sqlite3.connect("discord.db")
    cursor = db.cursor()
    cursor.execute("INSTERT INTO warns(guild_id, user_id, reason, author_id, date) VALUES(?, ?, ?, ?, ?)", (ctx.author.guild.id, member.id, reason, ctx.author.id, time.time()))
    cursor.close()
    db.commit()
    db.close()
    await ctx.send(f"Dodałeś warna użytkownikowi {member.name} z powodu {reason}")

bot.remove_command("help")

for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")

#Error Handling
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Taka komenda nie istnieje")
    if isinstance(error, commands.CommandOnCooldown):
            await ctx.send("Musisz poczekać przed kolejnym użyciem tej komendy")

with open("key.json","r") as key:
    data = json.load(key)
    bot.run(data.get("key"))