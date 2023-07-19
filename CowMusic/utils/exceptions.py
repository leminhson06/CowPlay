#
# Copyright (C) 2021-2022 by TeamCow@Github, < https://github.com/TeamCow >.
#
# This file is part of < https://github.com/TeamCow/CowMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamCow/CowMusicBot/blob/master/LICENSE >
#
# All rights reserved.


class AssistantErr(Exception):
    def __init__(self, errr: str):
        super().__init__(errr)
