import openai


# 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
class ChatgptService:
    def __init__(self):
        self.data = []

    def ask(self, question):
        openai.api_key = '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'

        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
            prompt="Write a tagline for an ice cream shop."
        )

        print(response['choices'][0]['message']['content'])
