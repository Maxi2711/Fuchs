from typing import Dict, List

from util.time_util import get_current_time_and_date


class Config:
    def __init__(self, server_id: int = 0, administrators: List[int] = [], moderators: List[int] = [], commands: List[dict] = [], warnings: List[dict] = [], bans: List[dict] = [], AMA: dict = {}, cogs: List[object] = []) -> None:
        self.server_id = server_id
        self.administrators = administrators
        self.moderators = moderators
        self.commands = commands
        self.warnings = warnings
        self.bans = bans
        self.AMA = AMA
        self.cogs = cogs
        self.warningid = 1
        self.banid = 1

    def __create_general_waning_ban(self,id: int, user: int, moderator: int, reason: str, time: str = get_current_time_and_date()) -> dict:
        output = {
            "id": id,
            "user": user,
            "moderator": moderator,
            "reason": reason,
            "time": time
        }
        return output

    def add_warning(self, user: int, moderator: int, reason: str) -> dict:
        output = self.__create_general_waning_ban(self.warningid,user,moderator,reason)
        self.warningid += 1
        return output

    def add_ban(self, user: int, moderator: int, reason: str) -> dict:
        output = self.__create_general_waning_ban(self.banid,user,moderator,reason)
        self.banid += 1
        return output    

    def remove_warning(self, id: int) -> None:
        self.warnings.remove(next((item for item in self.warnings if item["id"]==id), None))

    def remove_ban(self, id: int) -> None:
        self.bans.remove(next((item for item in self.bans if item["id"]==id), None))
    
    def remove_warnings(self, user: int) -> None:
        index = []
        for warning in self.warnings:
            if warning["user"] == user:
                index.append(self.warnings.index(warning))
        for i in range(len(index)):
            self.warnings.remove(self.warnings[index[len(index) - i - 1]])


    def create_command(self, name: str, access: List[int], code: str) -> dict:
        output = {
            "name": name,
            "access": access,
            "code": code
        }
        return output

    def create_question(self, user_id: int, user_name: str, user_dis: int, answered: bool, message_id: int, readbymod: bool, content: str, notes: str) -> dict:
        output = {
            "user_uuid": user_id,
            "author_name": user_name,
            "author_discriminator": user_dis,
            "message_content": content,
            "answered": answered,
            "id": message_id,
            "readbymoderator": readbymod,
            "notes": notes
        }
        return output

    def create_AMA(self, channel_id: int, prefix: List[str], askprefix: List[str]) -> dict:
        output = {
            "channel_id": channel_id,
            "prefix": prefix,
            "askprefix": askprefix,
            "questions": []
        }
        return output

    def dictionary(self) -> dict:
        output = {
            "server": self.server_id,
            "administrators": self.administrators,
            "moderators": self.moderators,
            "commands": self.commands,
            "warnings": self.warnings,
            "warningid": self.warningid,
            "bans": self.bans,
            "banid": self.banid,
            "AMA": self.AMA,
            "cogs": self.cogs
        } 

        print(output)
        return output

    def import_dictionary(self, dic: dict) -> None:
        self.server_id = dic["server"]
        self.administrators = dic["administrators"]
        self.moderators = dic["moderators"]
        self.commands = dic["commands"]
        self.warning = dic["warnings"]
        self.bans = dic["bans"]
        self.AMA = dic["AMA"]
        self.warningid = dic["warningid"]
        self.banid = dic["banid"]

    server_id: int  # Stores the servers ID the config file relates to
    administrators: List[int]  # Stores a list of IDs of all administrators
    moderators: List[int]  # Stores a list of IDs of all moderators
    commands: List[dict]  # Stores all custom commands

    warnings: List[dict]  # Stores all warned users
    warningid: int # Stores the current warning ID
    bans: List[dict]  # Stores all baned users
    banid: int # Stores the current ban ID

    AMA: dict # Stores the data for the AMA
    cogs: List[object] # Stores all the Cogs
