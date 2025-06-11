import os
import sys
import requests

def send_telegram_message(message):
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not bot_token or not chat_id:
        print("Error: TELEGRAM_BOT_TOKEN o TELEGRAM_CHAT_ID no están configurados")
        return

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}

    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print("Mensaje enviado a Telegram")
    else:
        print(f"Error al enviar mensaje: {response.text}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        msg = sys.argv[1]
        send_telegram_message(msg)
    else:
        print("No se proporcionó mensaje para Telegram")
