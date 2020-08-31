import discord
from discord.ext import commands
import numpy as np
import time

class Spin(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def spin(self, ctx):
	    """Spins the wheel!"""
	    x = np.random.uniform(0, 1)
	    print("x = ", x)
	    if x <= .40:
	        response = "You gain 1 point!"
	    elif x <= .60:
	        response = "You lose 1 point :("
	    elif x <= .80:
	        response = "You gain 5 points!"
	    elif x <= .85:
	        response = "You lose 5 points :("
	    elif x <= .90:
	        response = "Unlucky. You lose a turn."
	    elif x <= 1:
	        response = "Wow! You gain 10 points!"
	    await ctx.send("You spin the wheel...")
	    time.sleep(3)
	    await ctx.send("It spins around...")
	    time.sleep(3)
	    await ctx.send("It finally starts slowing down...")
	    time.sleep(3)
	    await ctx.send("You look at the result...")
	    time.sleep(3)
	    await ctx.send(response)

def setup(bot):
    bot.add_cog(Spin(bot))