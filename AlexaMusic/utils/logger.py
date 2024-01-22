# Copyright (C) 2024 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

""""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2024 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


from config import LOG, LOG_GROUP_ID, MUSIC_BOT_NAME
from AlexaMusic.utils.database import is_on_off
from AlexaMusic import app


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        logger_text = f"""
**━━━━━━━━━━━━━━━**
**{MUSIC_BOT_NAME} Music Logs **
**━━━━━━━━━━━━━━━**
**Chat Name: >** {message.chat.title} [`{message.chat.id}`]
**━━━━━━━━━━━━━━━**
**Name: ›** {message.from_user.mention}
**━━━━━━━━━━━━━━━**
**Username: ›** @{message.from_user.username}
**━━━━━━━━━━━━━━━**
**Id: ›** `{message.from_user.id}`
**━━━━━━━━━━━━━━━**
**Support: >** {chatusername}
**━━━━━━━━━━━━━━━**
**Searehed:** {message.text}
**━━━━━━━━━━━━━━━**
**Stream Type:** {streamtype}
**━━━━━━━━━━━━━━━**"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
