from typing import List
from enum import Enum
import os
import time
from util.time_util import get_current_time

def msg_type_string(key: int) -> str:
    switcher = {
        msg_type.INFO: "INFO",
        msg_type.WARNING: "WARNING",
        msg_type.ERROR: "ERROR"
    }
    return switcher.get(key, "Invalid ID")

class msg_type(Enum):
        INFO = 0,
        WARNING = 1,
        ERROR = 2 

class Log:
    def __init__(self) -> None:
        self.buffer = []
        self.reset_logfile()

    def __append_log(self, m: str, t: int, o: str) -> None:
        tmp = self.std_msg.format(msg_type_string(t),get_current_time(),o,m)
        self.buffer.append(tmp)

    def reset_logfile(self) -> None:
        open(self.std_path,"w").close()
        os.remove(self.std_path)

    def log(self, msg: str, type: int, origin: str) -> None:
        self.__append_log(msg,type,origin)
        if len(self.buffer) == 10:
            f = open(self.std_path,"a")
            for entry in self.buffer:
                f.write(entry)
            f.close()

            self.buffer = []
            self.count = 0

    std_path = "log.log"
    std_msg = "{0} [{1}] | {2} | {3}\n"
    buffer: List[str]