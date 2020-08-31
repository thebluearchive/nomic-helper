import discord
from discord.ext import commands
import numpy as np
import time

class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def poll(self, ctx):
        """Runs a poll, notifying when all eligible voters have voted."""
        print(ctx.author)
        print("Message =", ctx.message)
        await ctx.message.add_reaction('👍')
        await ctx.message.add_reaction('🤷')
        await ctx.message.add_reaction('👎')

        await ctx.send("@everyone Vote :angry:")

        for role in ctx.guild.roles:
            if role.name == 'Voter':
                voter_dict = {player.name: False for player in role.members}
        print("voter_dict =", voter_dict)

        def all_voted(voter_dict):
            """Confirms if everyone has voted"""
            all_have_voted = True
            for entry in voter_dict.values():
                if entry is False:
                    return False
            return True

        def next(ctx):
            """Determines whose turn is next"""
            for role in ctx.guild.roles:
                if role.name == 'Humans (?)':
                    players = [player.mention for player in role.members]
            next_player = np.random.choice(players)
            return next_player

        while True:
            reaction, user = await self.bot.wait_for('reaction_add')
            print("message = ", reaction.message)
            if ctx.message.id == reaction.message.id:
                if user.name in voter_dict:
                    voter_dict[user.name] = True
            if all_voted(voter_dict):
                await ctx.send("@everyone All votes have been cast!")
                voter_dict = {player.name: False for player in role.members}
                next_player = next(ctx)
                time.sleep(3)
                await ctx.send(next_player + ", you're up!")
                break
        return

def setup(bot):
    bot.add_cog(Poll(bot))