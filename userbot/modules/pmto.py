# ported from telebot
# i ported from shivam's project :) 

from userbot import CMD_HELP
from userbot.utils import admin_cmd
from userbot import bot as borg

@borg.on(admin_cmd(pattern="pmto ?(.*)"))
async def pmto(event):
    a = event.pattern_match.group(1)
    b = a.split(" ")
    chat_id = b[0]
    try:
        chat_id = int(chat_id)
    except BaseException:
        pass
    msg = "".join(f'{i} ' for i in b[1:])
    if not msg:
        return
    try:
        await borg.send_message(chat_id, msg)
        await event.edit("Message sent!")
    except BaseException:
        await event.edit("Something went wrong.")


CMD_HELP.update({"pmto": ".pmto <username> <message>"})
