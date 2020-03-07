from pyrogram import Client, MessageHandler

import settings


app = Client("my_account", api_id=settings.API_ID, api_hash=settings.API_HASH, proxy=settings.PROXY, plugins={"root":"plugins"})

if __name__ == '__main__':
    app.run()