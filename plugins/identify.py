from pyrogram import Client, Filters
import utils


@Client.on_message(utils.command("id"))
def ver(client, message):
    response = dict(Chat=dict(ID=message.chat.id), ThisMessage=message.message_id)
    if message.chat.type in ["bot", "supergroup", "channel"]:
        response["Chat"]["Restricted"] = message.chat.is_restricted
        if message.chat.is_restricted:
            for i, restrict in enumerate(message.chat.restrictions):
                response["Chat"][f"Restrict reason #{i}"] = dict(
                    Platform=restrict.platform,
                    Reason=restrict.reason,
                    Text=restrict.text
                )
    if message.reply_to_message:
        reply = message.reply_to_message
        response["Reply"] = {"Message": reply.message_id}
        if reply.from_user is not None:
            response["Reply"]["User"] = dict(ID=reply.from_user.id,
                                             Link=utils.HTMLStr(f'<a href="tg://user?id={reply.from_user.id})">🔗</a>'))
        if reply.entities is not None:
            response["Reply"]["Entities"] = list()
            for entity in reply.entities:
                if entity.user is not None:
                    response["Reply"]["Entities"].append({"ID": entity.user.id, "Name": entity.user.first_name,
                                                          "Link": utils.HTMLStr(
                                                              f'<a href="tg://user?id={entity.user.id})">🔗</a>')})
        file = None
        if reply.sticker is not None:
            response["Reply"]["Stickerpack set_name"] = reply.sticker.set_name
        for possible_file in [reply.photo, reply.animation, reply.sticker, reply.video, reply.voice, reply.video_note,
                              reply.audio, reply.sticker]:
            if possible_file is not None:
                file = possible_file
                break
        if file is not None:
            response["Reply"]["File ID"] = file.file_id
    utils.edit_message(message, response)
