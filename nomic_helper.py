import discord
from discord.ext import commands
import numpy as np

bot = commands.Bot(command_prefix = '!', description = "Nomic Helper Commands")

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def hello(ctx):
    """ Says 'Hello!' """
    await ctx.send('Hello!')

@bot.command()
async def rand(ctx, lower, upper):
    """ Generates a random integer between lower and upper, inclusive"""
    try:
        response = "Generating a random number between " + str(lower) + " and " + str(upper) + ". RNGesus declares " + str(np.random.randint(lower, upper))
    except Exception:
        response = "Arguments must be integers."
    await ctx.send(response)

bot.run(token)