import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from dotenv.main import resolve_variables

import blackjack
import bank
import checkbalance

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

client = commands.Bot(command_prefix = "$")

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name = GUILD)
    print(
        f"{client.user} is connected to the following guild:\n"
        f"{guild.name} (id: {guild.id})"
    )

@client.command()
async def bjhelp(ctx):
    bot_help = open("help.txt", "r")
    await ctx.send(bot_help.read())

@client.command()
async def register(ctx):
    bank.register(ctx.author, ctx.author.name, ctx.author.id)

@client.command()
async def money(ctx):
    money = bank.money(ctx.author)
    await ctx.channel.send("<@" + str(ctx.author.id) + ">\nCurrently you have: " + str(money) + "$")

@client.command(name = "blackjack")
async def blackjack_func(ctx, arg1):
    if checkbalance.check(ctx.author, arg1) == True:
        bank.handle_bet(ctx.author, arg1)
        result = blackjack.game(ctx.author, arg1)
        print(result)
        if result == "error":
            await ctx.channel.send("Error, command not known.")
        elif result == "draw":
            await ctx.channel.send("The game ended in a draw.")
            payout_draw = int(arg1) * -1
            bank.handle_bet(ctx.author, payout_draw)
        elif result == "won":
            await ctx.channel.send("Hey! You won!")
            payout_won = int(arg1) * -2
            bank.handle_bet(ctx.author, payout_won)
        elif result == "blackjack":
            await ctx.channel.send("Wow! You got a blackjack!")
            payout_blackjack = int(arg1) * -2.5
            bank.handle_bet(ctx.author, payout_blackjack)
        else:
            await ctx.channel.send("Oh, darn it! You lost...\nHow about another round?")
    else:
        await ctx.channel.send("I'm sorry, but your balance seems to be to low")

client.run(TOKEN)