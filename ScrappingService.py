class ScrappingService:
    def __init__(self, scrapper):
        self.scrapper = scrapper

    def scrap(self, url, file_name):
        file = open(file_name, 'w')

        scrapped_data = self.scrapper.scrap(url)
        file.write(scrapped_data)
        file.close()
