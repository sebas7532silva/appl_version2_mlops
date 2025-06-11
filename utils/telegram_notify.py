import requests

class TelegramNotifier:
    def __init__(self, bot_token: str, chat_id: str):
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.api_url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"

    def send_message(self, message: str):
        payload = {
            'chat_id': self.chat_id,
            'text': message,
            'parse_mode': 'Markdown'
        }
        try:
            response = requests.post(self.api_url, data=payload)
            if response.status_code == 200:
                print("Mensaje enviado a Telegram.")
            else:
                print(f"Error al enviar mensaje: {response.status_code}, {response.text}")
        except Exception as e:
            print(f"Exception al enviar mensaje: {e}")
