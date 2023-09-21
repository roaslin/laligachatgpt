# This is a sample Python script.

from chat_gpt_chat_client import ChatGPTChatClient
from chat_gpt_service import ChatgptService
from console import Console
from data_repository import DataRepository
from scrapper import Scrapper
from scrapping_service import ScrappingService


def la_liga_feature():
    scrapper = Scrapper()
    data_repository = DataRepository()
    scrapping_service = ScrappingService(scrapper, data_repository)

    scrapping_service.scrap('https://www.laliga.com/en-GB/laliga-easports/standing',
                            'scrapped_data_from_la_liga_standing.txt')

    chat_gpt_chat_client = ChatGPTChatClient()
    console = Console()
    chatgpt_service = ChatgptService(chat_gpt_chat_client, data_repository, 'chat_gpt_answers.txt', console,
                                     'scrapped_data_from_la_liga_standing.txt')

    chatgpt_service.ask('Who is the current leader of La Liga EA Sports?')
    chatgpt_service.ask('Which teams have more than 6 points?')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    la_liga_feature()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
