from discord.ext import commands
import discord
import logging
import data
import os

class Vaulter(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.data = data.Data(os.getenv("DATA_PATH"))
        self.bot = bot
        self.logger = logging.getLogger("discord.vaulter")
    
    @commands.command()
    async def ping(self, ctx):
        """Simple ping command"""
        self.logger.info(f"Ping used by {ctx.author}")
        await ctx.send(f'Pong! Latency: {round(self.bot.latency * 1000)}ms')
    
    @commands.command()
    async def store(self, ctx, *args):
        """Says hello to the user"""
        self.logger.info(f"Store used by {ctx.author}")
        await ctx.send(file=discord.File(r"D:\projects\pypystuff\bpVault\temp\e.txt"))

async def setup(bot:commands.Bot):
    await bot.add_cog(Vaulter(bot))