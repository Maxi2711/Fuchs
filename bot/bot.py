import sys
sys.path.append("../config/")

import discord
from discord.ext import commands 
from config.config_class import Config 

class Main(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.BOT = bot

    def __interpret_command()->None:
        pass

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.Cog.listener()
    async def on_message(self, message):
        pass
    
    BOT: commands.Bot
    config: Config

class Justice(commands.Cog):
    @commands.Cog.listener()
    async def ban(ctx, user, reason = ""):
        pass

    @commands.Cog.listener()
    async def unban(ctx, user):
        pass

    @commands.Cog.listener()
    async def warn(ctx, user, reason = ""):
        pass

    @commands.Cog.listener()
    async def unwarn(ctx, user):
        pass