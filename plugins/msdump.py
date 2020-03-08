from pyrogram import Client
import utils

@Client.on_message(utils.command(["dmp", "dump"]))
def msdump(client, message):
    if message.reply_to_message:
        utils.edit_message(message, message.reply_to_message.__dict__)
    else:
        message.edit_text("You forgot to reply to message, you dumb fuck")
