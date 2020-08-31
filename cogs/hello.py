import discord
from discord.ext import commands

class Hello(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def hello(self, ctx, *args):
		"""Says hello"""
		await ctx.send("Hello! I am currently online.")


def setup(bot):
    bot.add_cog(Hello(bot))