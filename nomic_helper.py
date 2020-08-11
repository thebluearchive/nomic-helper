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
    print("player =", player)
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

@bot.command()
async def poll(ctx):
    """Runs a poll, notifying when all eligible voters have voted."""
    print(ctx.author)
    print("Message =", ctx.message)
    await ctx.message.add_reaction('👍')
    await ctx.message.add_reaction('🤷')
    await ctx.message.add_reaction('👎')

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
            if role.name == 'Voter':
                players = [player.mention for player in role.members]
        next_player = np.random.choice(players)
        return next_player

    while True:
        reaction, user = await bot.wait_for('reaction_add')
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

bot.run(token)