from pyrogram import Client
import utils

@Client.on_message(utils.command("fetch"))
def fetch(client, message):
    if len(message.command) > 1:
        uid = message.command[1]
        try:
            utils.edit_message(message, {"Link": utils.HTMLStr(f'<a href="tg://user?id={uid})">🔗</a>')})
        except ValueError as e:
            utils.edit_message(message, {"Error": str(e)})
    else:
        message.edit_text("No ID Provided!")
