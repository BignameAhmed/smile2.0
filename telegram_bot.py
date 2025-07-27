import requests

BOT_TOKEN = "7754701186:AAGzNjIaz5C4Ollw-XR16y6kPl6w7S9Ompc"
CHAT_ID = "5599152796"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    requests.post(url, data=payload)