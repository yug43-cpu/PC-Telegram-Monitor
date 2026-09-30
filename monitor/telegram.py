import os
import requests
from dotenv import load_dotenv


load_dotenv()


BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def send_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": message
    }

    response = requests.post(
        url,
        data=data,
        timeout=10
    )

    if response.ok:
        result = response.json()
        return result["result"]["message_id"]

    print("Telegram Error:")
    print(response.text)

    return None


def edit_message(message_id, message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/editMessageText"

    data = {
        "chat_id": CHAT_ID,
        "message_id": message_id,
        "text": message
    }

    response = requests.post(
        url,
        data=data,
        timeout=10
    )

    if response.ok:
        return True

    print("Telegram Edit Error:")
    print(response.text)

    return False