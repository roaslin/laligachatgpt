class ChatgptService:
    def __init__(self, chat_gpt_client, data_repository):
        self.data_repository = data_repository
        self.chat_gpt_client = chat_gpt_client

    def ask(self, question):
        pass

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
