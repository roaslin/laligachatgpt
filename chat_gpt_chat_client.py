import requests


class ChatGPTChatClient:
    def __init__(self):
        pass

    # Post a text to ChatGPT either question/data to the context window
    def send(self, text, context):
        # api_key should be stored in the cloid i.e: AWS Secrets manager
        open_ai_api_key = 'YOUR_KEY_GOES_HERE'
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
