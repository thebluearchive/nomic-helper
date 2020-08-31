import discord
from discord.ext import commands
import numpy as np
import time

class Attack(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def attack(self, ctx, player):
	    """Attacks another player!"""
	    x = np.random.uniform(0, 1)
	    print("x = ", x)
	    print("player =", player)
	    if x <= .40:
	        response = "Your attack fails! No damage is dealt."
	    elif x <= .70:
	        response = "Your attack is successful! " + player + " loses 5 hp."
	    elif x <= .85:
	        response = "You strike hard! " + player + " loses 10 hp."
	    elif x <= .99:
	        response = "In one swift, clumsy movement, you manage to damage yourself for 15 hp."
	    elif x <= 1:
	        response = "Critical hit! Your opponent loses 100 hp!"
	    await ctx.send("You attack " + player + "!")
	    time.sleep(3)
	    await ctx.send(response)

def setup(bot):
    bot.add_cog(Attack(bot))