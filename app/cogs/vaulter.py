from discord.ext import commands
import logging

class Vaulter(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        self.logger = logging.getLogger("discord.vaulter")
    
    @commands.command()
    async def ping(self, ctx):
        """Simple ping command"""
        self.logger.info(f"Ping used by {ctx.author}")
        await ctx.send(f'Pong! Latency: {round(self.bot.latency * 1000)}ms')
    
    @commands.command()
    async def hello(self, ctx):
        """Says hello to the user"""
        self.logger.info(f"Hello command used by {ctx.author}")
        await ctx.send(f"Hello {ctx.author.name}!")

async def setup(bot:commands.Bot):
    await bot.add_cog(Vaulter(bot))