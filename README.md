# laligachatgpt 🤖

## Logic behind the solution

I imagined 2 separate main services:

 -  **scraping_service.py** => scraps single urls and stores scrapped data
 -  **chat_gpt_service.py** => Interacts with ChatGPT ⚠️ I had issues 😖 with my python and the API versions, so I had to call the endpoints manually ✋ ⚠️

Then there are some other modules that are used by those 2 services, more info in the codebase

## Run tests:

I used Outside-in TDD to complete the code (while learning python T_T) so you should start at:
  - Acceptance test is **la_liga_feature_test.py** 
     - I had to use an interceptor to return fake Response objects from the API, couldn't create one manually, the Response api didn't allow me or I didn't see how to T_T
  - Run test `python la_liga_feature_test.py`
  - There are specific unit tests for the services and other modules, except all those modules implementing code that is not ours. Those classes are **mocked/stubbed**.

## Steps to run: 🏃

  1. Go to file 📁 **chat_gpt_chat_client.py** and add your **api_key** 🔑, find `YOUR_KEY_GOES_HERE` in the file and replace it.
     - Where to get and API key => [ChatGPT API keys](https://platform.openai.com/account/api-keys)
  3. Without a **Dockerized** 🐳 version (sorry for this T_T) you should install all the required dependencies:
     - Run command `pip install -r requirements.txt` ⚠️MAKE SURE TO USE A VENV⚠️
  4. Run command `python main.py` to let the magic flow ✨
  5. You should find two files in the root of the project when the execution ends
     - **chat_gpt_answers.txt** contains the two answered questions from ChatGPT
     - **scrapped_data_from_la_liga_standing.txt** contains the data scrapped from [LaLiga EA Sports Standing](https://www.laliga.com/en-GB/laliga-easports/standing)
  6. Check answers in the console
