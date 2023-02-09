#
# Copyright (C) 2021-2022 by TeamInflex@Github, < https://github.com/TeamInflex >.
#
# This file is part of < https://github.com/TeamInflex/InflexMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamInflex/InflexMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from InflexMusic.core.bot import InflexBot
from InflexMusic.core.dir import dirr
from InflexMusic.core.git import git
from InflexMusic.core.userbot import Userbot
from InflexMusic.misc import dbb, heroku, sudo

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
app = InflexBot()

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
