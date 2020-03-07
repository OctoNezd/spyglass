import subprocess

from pyrogram import Client, Filters
from pyrogram import __version__ as pyrogramver
import utils
try:
    commit = subprocess.check_output("git rev-parse --short HEAD", shell=True, stderr=subprocess.STDOUT)
except subprocess.CalledProcessError as e:
    commit = e.output

@Client.on_message(Filters.text & Filters.outgoing & Filters.command("ver", prefixes="sg!") & ~Filters.incoming)
def ver(client, message):
    response = {"Spyglass": {"commit":""}, "Pyrogram": {"version": pyrogramver}}
    utils.edit_message(message, response)

