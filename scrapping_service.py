class ScrappingService:
    def __init__(self, scrapper, repository):
        self.repository = repository
        self.scrapper = scrapper

    # Scraps and stores data in a file
    def scrap(self, url, file_name):
        scrapped_data = self.scrapper.scrap(url)
        self.repository.store(file_name, scrapped_data)
