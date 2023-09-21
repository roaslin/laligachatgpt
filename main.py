# This is a sample Python script.

from data_repository import DataRepository
from scrapping_service import ScrappingService
from scrapper import Scrapper


def print_hi(name):
    scrapper = Scrapper()
    data_repository = DataRepository()
    scrapper_service = ScrappingService(scrapper, data_repository)

    scrapper_service.scrap('https://www.laliga.com/en-GB/laliga-easports/standing',
                           'scrapped_data_from_la_liga_standing.txt')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
