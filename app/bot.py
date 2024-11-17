import discord
import logging

class Bot(discord.Client):
    def __init__(self, *, intents, **options):
        super().__init__(intents=intents, **options)
        self.logger = logging.getLogger("discord.bot")

    async def on_ready(self):
        self.logger.info(f"Logged on as {self.user}")

    async def on_message(self, message:discord.Message):
        self.logger.info(f"Message from {message.author} in {message.channel}: {message.content}")