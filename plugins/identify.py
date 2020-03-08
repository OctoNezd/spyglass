
from pyrogram import Client, Filters
import utils

@Client.on_message(utils.command("id"))
def ver(client, message):
    response = dict(Chat=message.chat.id, ThisMessage=message.message_id)
    if message.reply_to_message:
        reply = message.reply_to_message
        response["Reply"] = {"Message":reply.message_id}
        if reply.from_user is not None:
            response["Reply"]["User"] = dict(ID=reply.from_user.id, Link=utils.HTMLStr(f'<a href="tg://user?id={reply.from_user.id})">🔗</a>'))
        if reply.entities is not None:
            response["Reply"]["Entities"] = list()
            for entity in reply.entities:
                if entity.user is not None:
                    response["Reply"]["Entities"].append({"ID": entity.user.id, "Name": entity.user.first_name, "Link": utils.HTMLStr(f'<a href="tg://user?id={entity.user.id})">🔗</a>')})
        if reply.sticker is not None:
            response["Reply"]["Stickerpack set_name"] = reply.sticker.set_name
    utils.edit_message(message, response)

