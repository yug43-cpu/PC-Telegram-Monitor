import json
import os


DATA_FILE = os.path.join(
    os.path.dirname(__file__),
    "monitor_data.json"
)


def load_data():
    if not os.path.exists(DATA_FILE):
        return {}

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        return {}


def save_data(data):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    except OSError as error:
        print("Storage Error:")
        print(error)