# Repository to store chatgpt answers
# IMHO this should be implementing an interface, so we can have different repo implementations
class DataRepository:
    def __init__(self):
        pass

    def read(self, file_name):
        file = open(file_name, 'r')
        data = file.read()
        file.close()

        return data

    def store(self, file_name, data):
        file = open(file_name, 'a')
        file.write(data)
        file.close()
