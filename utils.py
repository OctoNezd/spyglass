import html

def generate_tree(dictionary, level=0):
    lines = []
    if isinstance(dictionary, list):
        dictionary = dict(enumerate(dictionary))
    for key, value in dictionary.items():
        key = str(key)
        line = f"<b>{html.escape(key)}</b>:"
        if isinstance(value, dict) or isinstance(value, list):
            line += "\n" + generate_tree(value, level+1)
        else:
            line += str(value)
        lines.append("-" * level + line)
    return "\n".join(lines)



def edit_message(message, dictionary):
    message.edit_text(generate_tree(dictionary))

if __name__ == '__main__':
    import json
    with open("sample.json") as f:
        data = json.load(f)

    with open("sample.html", "w") as f:
        f.write(generate_tree(data).replace("\n", "<br/>"))