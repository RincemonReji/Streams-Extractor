#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


import os

class Config(object):

    # Get a bot token from botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1658538479:AAExMFTX1ywKg9yyeWWUJs21urPg_qpFHKY")


    # Get from my.telegram.org (or @UseTGXBot)
    APP_ID = int(os.environ.get("APP_ID", "2092738"))
    API_HASH = os.environ.get("API_HASH", "77149d5b934f4823df42ee742ba337a1")
    
