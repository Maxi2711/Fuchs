import time
import sys  # For sys.argv

from discord.ext import commands

from bot.bot import Main
from config.config_class import Config
from config.config_io import Config_IO as cio
import random as rnd
import log.log as log

from util.time_util import get_current_time_and_date

def start() -> None:
    logger = log.Log()
    logger.reset_logfile()

    # if len(sys.argv) < 2:
    #     print("Please provide a token as command line argument.")
    #     return

    test = Config()

    test.server_id = 789683776846168145

    test.administrators.append(813508402944540704)
    test.moderators.append(363314139436810241)
    test.commands.append({"Name":"print_c","Access":813508402944540704,"Code":"def print_c(ctx, msg: str):\n\tprint(msg)"})
    test.warnings.append(test.create_warning(363314139436810241,813508402944540704,"Fox"))
    test.bans.append(test.create_warning(363314139436810241,813508402944540704,"Fox"))
    # Config = cio.load_config("Test.cfg")
    cio.save_config(test, "test.json")
    # print(test.dictionary())
    bot = commands.Bot(None)
    bot.add_cog(Main(bot))


if __name__ == "__main__":
    start()
    print(get_current_time_and_date())