import discord
from discord.ext import commands
import numpy as np
import time

class Rand(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def rand(self, ctx, lower, upper):
	    """ Generates a random integer between lower and upper, inclusive"""
	    try:
	        new_upper = int(upper) + 1
	        lower = int(lower)
	        print("lower = ", lower, "; upper =", new_upper)
	        number = np.random.randint(lower, new_upper)
	        print("number =", number)
	        await ctx.send("Generating a random number between " + str(lower) + " and " + str(upper) + "...")
	        time.sleep(3)
	        await ctx.send("RNGesus declares " + str(number) + ".")
	    except Exception:
	        await ctx.send("Arguments must be integers, with the first integer lower than the next.")

def setup(bot):
    bot.add_cog(Rand(bot))