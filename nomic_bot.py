import discord
from discord.ext import commands
# in the future, consider logging info using
# import logging

extensions = (
    "cogs.hello",
    "cogs.rand",
    "cogs.spin",
    "cogs.attack",
    "cogs.poll",
    )

class Nomic_Bot(commands.Bot):
    def __init__(self, token):
        super().__init__(
            command_prefix = '!',
            status = discord.Status.online,
            activity = discord.Game(name = "Nomic!"))
        self.token = token

        for extension in extensions:
            self.load_extension(extension)

    async def on_ready(self):
        print("Logged in as:")
        print("Name: {}".format(self.user.name))
        print("ID: {}".format(self.user.id))

    def run(self):
        super().run(self.token, reconnect=True)