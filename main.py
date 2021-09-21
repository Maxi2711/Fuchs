import time
import sys  # For sys.argv

from discord.ext import commands

from bot.bot import Main
from config.config_class import Config
from config.config_io import Config_IO as cio
from bot.bot import Bot
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
    test.warnings.append(test.add_warning(363314139436810241,813508402944540704,"Fox"))
    test.warnings.append(test.add_warning(363314139436810241,813508402944540704,"Fox"))
    test.warnings.append(test.add_warning(363314139436810242,813508402944540704,"Fox"))
    test.warnings.append(test.add_warning(363314139436810241,813508402944540704,"Fox"))
    test.warnings.append(test.add_warning(363314139436810244,813508402944540704,"Fox"))
    test.bans.append(test.add_ban(363314139436810241,813508402944540704,"Fox"))
    test.AMA = test.create_AMA(869938839102291988,["Q","W"],["A"])
    test.AMA["questions"].append(test.create_question(813508402944540704,
    "Felix", 1234, False,
    813508402944540704, False,
    "This is a test question",
    "These are test notes"))
    test.AMA["questions"].append(test.create_question(813508402944540704,
    "Felix", 1234, False,
    813508402944540704, False,
    "This is a second test question",
    "These are test notes"))
    test.remove_warnings(363314139436810242)

    # Config = cio.load_config("Test.cfg")
    cio.save_config(test, "test.json")
    # print(test.dictionary())
    bot = Bot("123", "test.json")
    bot._add_cog(Main)
    bot._remove_cog(Main)

if __name__ == "__main__":
    start()
    print(get_current_time_and_date())