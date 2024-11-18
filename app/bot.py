import discord
from discord.ext import commands
import logging

class Bot(commands.Bot):
    def __init__(self, *, intents, **options):
        super().__init__(command_prefix="!", intents=intents, **options)
        self.logger = logging.getLogger("discord.bot")

    async def setup_hook(self):
        await self.load_extension("cogs.vaulter")
        self.logger.info("Loaded all cogs")

    async def on_ready(self):
        self.logger.info(f"Logged on as {self.user}")

    async def on_message(self, message:discord.Message):
        self.logger.info(f"Message from {message.author} in {message.channel}: {message.content}")
        await self.process_commands(message)