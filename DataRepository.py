class DataRepository:
    def __init__(self):
        pass

    def read(self, file_name):
        file = open(file_name, 'r')
        return file.read()
