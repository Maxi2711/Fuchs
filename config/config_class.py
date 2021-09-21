from typing import Dict, List
from util.time_util import get_current_time_and_date


class Config:
    def __init__(self, server_id: int = 0, administrators: List[int] = [], moderators: List[int] = [], commands: List[dict] = [], warnings: List[dict] = [], bans: List[dict] = []) -> None:
        self.server_id = server_id
        self.administrators = administrators
        self.moderators = moderators
        self.commands = commands
        self.warnings = warnings
        self.bans = bans

    def create_warning(self, user: int, moderator: int, reason: str) -> dict:
        output = {
            "User": user,
            "Moderator": moderator,
            "Reason": reason,
            "Time": get_current_time_and_date()
        }
        return output

    def create_command(self, name: str, access: List[int], code: str) -> dict:
        output = {
            "Name": name,
            "Access": access,
            "Code": code
        }

    def dictionary(self) -> dict:
        output = {
            "Server": int,
            "Administrators": [],
            "Moderators": [],
            "Commands": [],
            "Warnings": [],
            "Bans": []
        }

        output["Server"] = self.server_id

        for user in self.administrators:
            output["Administrators"].append(user)

        for user in self.moderators:
            output["Moderators"].append(user)

        for command in self.commands:
            output["Commands"].append(command)

        for warning in self.warnings:
            output["Warnings"].append(warning)

        for ban in self.bans:
            output["Bans"].append(ban)

        return output

    def import_dictionary(self, dic: dict) -> None:
        self.server_id = dic["Server"]
        self.administrators = dic["Administrators"]
        self.moderators = dic["Moderators"]
        self.commands = dic["Commands"]
        self.warning = dic["Warnings"]

    server_id: int  # Stores the servers ID the config file relates to
    administrators: List[int]  # Stores a list of IDs of all administrators
    moderators: List[int]  # Stores a list of IDs of all moderators
    commands: List[dict]  # Stores all custom commands
    warnings: List[dict]  # Stores all warned users
    bans: List[dict]  # Stores all baned users
