#
# Copyright (C) 2021-2022 by TeamCow@Github, < https://github.com/TeamCow >.
#
# This file is part of < https://github.com/TeamCow/CowMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamCow/CowMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from CowMusic.core.bot import CowBot
from CowMusic.core.dir import dirr
from CowMusic.core.git import git
from CowMusic.core.userbot import Userbot
from CowMusic.misc import dbb, heroku, sudo

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = CowBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
