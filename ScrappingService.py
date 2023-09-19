class ScrappingService:
    def __init__(self):
        self.data = []

    def scrap(self, url, file_name):
        file = open(file_name, 'w')
        file.close()
