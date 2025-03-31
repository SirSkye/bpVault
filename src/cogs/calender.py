from discord.ext import commands
import discord
import logging
import data
import os

class Calender(commands.cog):
    def __init__(self, bot:commands.bot):
        self.logger = logging.getLogger("discord.calender")
    
    #@commands.command()