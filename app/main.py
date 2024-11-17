from dotenv import load_dotenv
import discord
import os
from bot import Bot
import logging

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = Bot(intents=intents)
client.run(os.getenv("DISCORD_TOKEN"))