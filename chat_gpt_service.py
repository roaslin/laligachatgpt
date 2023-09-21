class ChatgptService:
    def __init__(self, chat_gpt_client, data_repository, output_filename, console):
        self.chat_gpt_client = chat_gpt_client
        self.data_repository = data_repository
        self.output_filename = output_filename
        self.console = console

    # Logic for asking a question
    def ask(self, question):
        # Send question
        response = self.chat_gpt_client.send(question)
        response_json = response.json()

        if response.ok:
            # get answer, store and print it
            data = response_json['choices'][0]['message']['content']
            self.data_repository.store(self.output_filename, data)

            for line in data.splitlines():
                self.console.println(line)
        else:
            return response_json['error']

    # Updates context window
    def update_context_window_with(self, filename):
        try:
            data = self.data_repository.read(filename)
        except FileNotFoundError:
            return 'file-not-found'

        response = self.chat_gpt_client.send(data)

        if not response.ok:
            return 'error-updating-context-window'
        else:
            return 'context-window-updated'
