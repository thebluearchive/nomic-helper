import discord
from discord.ext import commands
import numpy as np
import time

bot = commands.Bot(command_prefix = '!', description = "Nomic Helper Commands")
NUM_PLAYERS = 2


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
        number = np.random.randint(lower, upper + 1)
        await ctx.send("Generating a random number between " + str(lower) + " and " + str(upper) + "...")
        time.sleep(3)
        await ctx.send("RNGesus declares " + str(np.random.randint(lower, upper)) + ".")
    except Exception:
        await ctx.send("Arguments must be integers, with the first integer lower than the next.")

@bot.command()
async def spin(ctx):
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


@bot.command()
async def attack(ctx, player):
    """Attacks another player!"""
    x = np.random.uniform(0, 1)
    print("x = ", x)
    if x <= .40:
        response = "Your attack fails! No damage is dealt."
    elif x <= .70:
        response = "Your attack is succesful! " + player + " loses 5 hp."
    elif x <= .85:
        response = "You strike hard! " + player + " loses 10 hp."
    elif x <= .99:
        response = "In one swift, clumsy movement, you manage to damage yourself for 15 hp."
    elif x <= 1:
        response = "Critical hit! Your opponent loses 100 hp!"
    await ctx.send("You attack " + player + "!")
    time.sleep(3)
    await ctx.send(response)

# @bot.command()
# async def react(ctx):
#     """Testing bot's reaction capabilities"""
#     print(ctx)
#     print(ctx.author)
#     print(ctx.message)
#     await ctx.message.add_reaction('👍')
#     await ctx.message.add_reaction('🤷')
#     await ctx.message.add_reaction('👎')
    
#     # def reaction_count(reactions):
#     #     """
#     #     counts the total number of reactions
#     #     """
#     #     count = 0
#     #     for reaction in reactions:
#     #         count += reaction.count
#     #     return count
#     vote_dict = {player: False for player in Voter.members}
#     while True:
#         user, reaction = await bot.wait_for('reaction_add')
#         print(user)
#         print(reaction)
#         # await ctx.send("@everyone All votes have been cast!")

## add !turn
## implemented through random.choice(humans)
bot.run(token)