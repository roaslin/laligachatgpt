class ChatgptService:
    def __init__(self, data_filename):
        self.data_filename = data_filename

    def ask(self, question):
        file = open(self.data_filename, 'r')
