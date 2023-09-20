class ChatgptService:
    def __init__(self, chat_gpt_client, data_repository, output_filename):
        self.chat_gpt_client = chat_gpt_client
        self.data_repository = data_repository
        self.output_filename = output_filename

    def ask(self, question):
        response = self.chat_gpt_client.send(question)
        response_json = response.json()

        if response.ok:
            data = response_json['choices'][0]['message']['content']
            self.data_repository.store(self.output_filename, data)
            return data
        else:
            return response_json['error']

    def updateContextWindowWith(self, filename):
        try:
            data = self.data_repository.read(filename)
        except FileNotFoundError:
            return 'file-not-found'

        response = self.chat_gpt_client.send(data)

        if not response.ok:
            return 'error-updating-context-window'
        else:
            return 'context-window-updated'
