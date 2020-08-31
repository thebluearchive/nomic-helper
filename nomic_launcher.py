import discord
from nomic_bot import Nomic_Bot
import sys

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

bot = Nomic_Bot(token)
bot.run()