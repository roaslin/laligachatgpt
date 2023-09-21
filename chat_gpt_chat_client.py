import requests


class ChatGPTChatClient:
    def __init__(self):
        pass

    # Post a text to ChatGPT either question/data to the context window
    def send(self, text, context):
        open_ai_api_key = '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'
        headers = {"Content-Type": "application/json",
                   "Authorization": "Bearer " + open_ai_api_key}
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": "".join(context)
                },
                {
                    "role": "user",
                    "content": "".join(text)
                }
            ]

        }

        return requests.post('https://api.openai.com/v1/chat/completions', json=data, headers=headers)
