import discord
import numpy as np

client = discord.Client()

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@client.command()
async def rand(ctx, lower, upper):
	if type(upper) == int and type(lower) == int:
		await.ctx.send("Generating a random number between "
			+ lower + "and" + upper ":" + np.random.randint())
	else:
		await.ctx.send("Arguments must be integers.")

client.run(token)