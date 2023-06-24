import sys, clipboard, json

SAVED_DATA = "clipboard.json"


def save_items(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except:
        return {}


if len(sys.argv) == 2:
    data = load_data(SAVED_DATA)
    match sys.argv[1]:
        case "save":
            key = input("Enter a key: ")
            data[key] = clipboard.paste()
            save_items(SAVED_DATA, data)
            print("saved")

        case "load":
            key = input("Enter a key: ")
            if key in data:
                clipboard.copy(data[key])
                print("copied")
            else:
                print("not found. The key doesn't seem to exist")

        case "list":
            print(data)
        case _:
            print("unknown command")

else:
    print("usage: python clipboard.py save|load|list")
