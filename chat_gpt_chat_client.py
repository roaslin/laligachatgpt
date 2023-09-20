import requests


class ChatGPTChatCLient():
    def __init__(self):
        pass

    def send(self, text):
        open_ai_api_key = ''
        headers = {"Content-Type": "application/json",
                   "Authorization": "Bearer " + open_ai_api_key}
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "user",
                    "content": "".join(text)
                }
            ]

        }

        return requests.post('https://api.openai.com/v1/chat/completions', json=data, headers=headers)

