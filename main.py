# bot.py
import os
import requests
import albion
import json
import discord

from discord.ext import commands

TOKEN = os.environ.get('DOOTDOOT_TOKEN')

bot = commands.Bot(command_prefix=",")


win_id = "LFMfbk-wS96vNKVQHzmfTQ"


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name="exit")
async def exit(ctx):
    if ctx.author == bot.user or ctx.channel.name != "bot":
        return
    await ctx.bot.close()

@bot.command(name="ohi")
async def ohi(ctx):
    #returns if message was from bot or not in bot channel
    if ctx.author == bot.user or ctx.channel.name != "bot":
        return
    await ctx.send("suh")

# searches albion  api for guild and users
@bot.command(name="search")
async def kd(ctx, arg1=None, arg2=None):
    if ctx.author == bot.user or ctx.channel.name != "bot":
        return
    if arg1 == None:
        await ctx.send("```usage: ,search [OPTION] user/guild name\n"
            "\t-p, displays only player results\n"
            "\t-g, displays only guild results```")
    if arg1 == "-p" or arg1 == "-g":
        if arg2 == None:
            await ctx.send("```usage: ,search [OPTION] user/guild name\n"
                "\t-p, displays only player results\n"
                "\t-g, displays only guild results```")
        else:
            await ctx.send(albion.search(arg1, arg2))
    else:
        await ctx.send(albion.search(arg1))
        

@bot.command(name="colours")
async def colours(ctx):
    stats = albion.get_kd(win_id)
    text = f"""```diff
+kill fame: {stats["kill_fame"]}```
```diff
- death fame: {stats["death_fame"]}```
```fix
kd: {stats["kd"]}```"""
    await ctx.send(text)

@bot.command(name="arbenasloxas")
async def benas(ctx):
    await ctx.send("jo :)")

@bot.command(name="shungite")
async def shungite(ctx):
    await ctx.send("Anyways uhm… I bought a whole bunch of, uh, SHUNGITE….. rocks……. "
    "do you know what shungite is? Anybody know what shungite is? No, not Suge Knight, "
    "I think hes locked up in prison. I'm talking SHUNGITE. Anyways, it's a 2 billion year old…. "
    "like… rock….. stone that protects against frequencies and unwanted frequencies that may be "
    "traveling in the air. So that's my story. I bought a whole bunch of stuff, put them around "
    "the La Casa. Little pyramids.")

@bot.command(name="embed")
async def embed(ctx, arg1=None):
    if ctx.author == bot.user or ctx.channel.name != "bot":
        return
    if(arg1 == None):
        await ctx.send("```usage: ,embed message```")
    else:
        embed = discord.Embed(title="omg!", description=arg1, url="https://www.sendbeestomars.com",
            image="https://discordemoji.com/assets/emoji/PepeHands.png", color=0x00FF00)
        embed.set_footer(text="what arm thing homie", icon_url="https://discordemoji.com/assets/emoji/PepeHands.png")
        embed.set_author(name="who?", url="https://discordemoji.com/assets/emoji/9452_lul.png")
        await ctx.send(embed=embed)

bot.run(TOKEN)