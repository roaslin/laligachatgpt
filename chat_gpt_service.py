class ChatgptService:
    def __init__(self, chat_gpt_client, data_repository, output_filename, console, context_filename):
        self.chat_gpt_client = chat_gpt_client
        self.data_repository = data_repository
        self.output_filename = output_filename
        self.console = console
        self.context_filename = context_filename
        self._context = ''

    # Logic for asking a question
    def ask(self, question):
        # store the context in memory, ideally we should be updating this context
        if self._context == '':
            try:
                self._context = self.data_repository.read(self.context_filename)
            except FileNotFoundError:
                return 'context-file-not-found'

        # Send question
        response = self.chat_gpt_client.send(question, self._context)
        response_json = response.json()

        if response.ok:
            # get answer, store and print it
            data = response_json['choices'][0]['message']['content']
            self.data_repository.store(self.output_filename, data)

            for line in data.splitlines():
                self.console.println(line)
        else:
            self.console.println(f"Error - {response_json['error']}")
            return response_json['error']
