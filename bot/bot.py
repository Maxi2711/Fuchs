from config.config_io import Config_IO
import sys
sys.path.append("../config/")

import discord
from discord.ext import commands 
from config.config_class import Config 

class Bot(commands.Bot):
    def __init__(self, token: str, config_path: str):
        self.bot = commands.Bot(None)
        self.token = token
        self.config = Config_IO.load_config(config_path)
    
    def _add_cog(self, cog: object) -> None:
        self.bot.add_cog(cog(self.bot))

    def _remove_cog(self, cog: object) -> None:
        self.bot.remove_cog(cog)

    def _run(self):
        self.bot.run(self.token)

    bot: commands.Bot
    config: Config
    token: str

class Main(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    def __interpret_command()->None:
        pass

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.Cog.listener()
    async def on_message(self, message):
        pass
    
    bot: commands.Bot
    config: Config

class Justice(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ban(ctx, user, reason = ""):
        pass

    @commands.command()
    async def unban(ctx, user):
        pass

    @commands.command()
    async def warn(ctx, user, reason = ""):
        pass

    @commands.command()
    async def unwarn(ctx, user):
        pass

    bot: commands.Bot