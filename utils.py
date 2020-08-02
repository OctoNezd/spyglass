import html
import time

from pyrogram import Filters, Object

class HTMLStr(str):
    pass

def command(command):
    return Filters.text & Filters.outgoing & Filters.command(command, prefixes="sg!") & ~Filters.forwarded

def generate_tree(dictionary, level=0):
    lines = []
    if isinstance(dictionary, list):
        dictionary = dict(enumerate(dictionary))
    for key, value in dictionary.items():
        key = str(key)
        line = f"<b>{html.escape(key)}</b>: "
        if not (value is None or key.startswith("_")):
            if isinstance(value, Object):
                value = value.__dict__
            if isinstance(value, dict) or isinstance(value, list):
                line += "\n" + generate_tree(value, level+1)
            elif isinstance(value, HTMLStr):
                line += value
            else:
                line += f"<code>{html.escape(str(value))}</code>"
            lines.append(html.escape("\u202f" * level) + line)
    return "\n".join(lines)



def edit_message(message, dictionary, delete_soon=False):
    message.edit_text(generate_tree(dictionary))
    if delete_soon:
        time.sleep(3)
        message.delete()

if __name__ == '__main__':
    import json
    with open("sample.json") as f:
        data = json.load(f)

    with open("sample.html", "w") as f:
        f.write(generate_tree(data).replace("\n", "<br/>"))