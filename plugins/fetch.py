from pyrogram import Client, Filters
import utils

@Client.on_message(Filters.text & Filters.outgoing & Filters.command("fetch", prefixes="sg!") & ~Filters.incoming)
def fetch(client, message):
    if len(message.command) > 1:
        uid = message.command[1]
        message.edit_text(f"[Permalink to {uid}](tg://user?id={uid})", parse_mode='markdown')
    else:
        message.edit_text("No ID Provided!")
