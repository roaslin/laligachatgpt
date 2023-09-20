class DataRepository:
    def __init__(self):
        pass

    def read(self, file_name):
        raise NotImplementedError

    def store(self, file_name, data):
        file = open(file_name, 'a')

        file.close()