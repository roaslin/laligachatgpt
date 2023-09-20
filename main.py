# This is a sample Python script.
import requests
from requests import Response

from ScrappingService import ScrappingService
from scrapper import Scrapper


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    scrapper = Scrapper()
    scrapper_service = ScrappingService(scrapper)

    scrapper_service.scrap('https://www.laliga.com/en-GB/laliga-easports/standing', 'test.txt')

    # service = ChatgptService()
    # service.ask("This is not working")

    file = open('test.txt', 'r')

    laliga_data = file.read()
    # print(laliga_data)
    open_ai_api_key = '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'
    headers = {"Content-Type": "application/json",
               "Authorization": "Bearer " + open_ai_api_key}
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "".join(laliga_data)
            },
            {
                "role": "user",
                "content": "Who is the current leader of La Liga EA Sports?"
            }
        ]

    }
    response = Response()
    Response
    request = requests.post('https://api.openai.com/v1/chat/completions', json=data, headers=headers)

    responsejson = request.json()
    print('Response json')
    print(responsejson)
    if request.ok:

        print('noe errors!')
        print(responsejson['choices'][0]['message']['content'])
    else:
        print('Exist error')
        print(responsejson['error'])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
