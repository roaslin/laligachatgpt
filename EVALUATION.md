Coding Challenge Evaluation
========

Overall evaluation
----
* **I couldn't generate the desired output** The file `chat_gpt_answers.txt` didn't get generated and no console error was provided either.
* The code lacks best practices (as described in Critical/Major/Minor issues below)
* **Overall the code looks FINE! ⭐️**

Critical issues ☣️
---
1. The API was returning error - `{'message': "This model's maximum context length is 4097 tokens. However, your messages resulted in 12677 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}` that you didn't capture anywhere and warned of it either in `main.py:24` or `chat_gpt_service.py:31` I had to add in `chat_gpt_service.py` the snippet `self.console.println(f"Error - {response_json['error']}")` to understand what was going on. This change is committed with the evaluation

Major issues ⚠️
----
1. The code doesn't throw any error either on console or exit messages if the openAI connection couldn't be made because the key was absent/incorrect.
1. Too many dependencies in the requirements file for such a small challenge.
2. The dependencies are hardcoded to versions, which is OK for reliability but in your case, you've hardcoded some really old versions which broke my 💻 For example you used `4.1.1` of https://pypi.org/project/typing-extensions/#history which is from **Feb 2022** 🥺 
2. The Unit Tests couldn't be executed the __standard__ way - `python3 -m unittest`
3. `console.py` is not required, usage of standard python logging library is expected - https://docs.python.org/3/library/logging.html
4. Doesn't use a configuration system/dotenv to get variables from the filesystem, especially OpenAI key (https://pypi.org/project/python-dotenv/)
5. No .gitignore to ignore the generated files which shouldn't be committed to the repository.

Minor issues
---
1. The code is very "Java-Like" - Usage of Repositories, Services, over-usage of Classes, static methods where pythonic modules could be sufficient. Which is __not-bad__ and __expected__ since you come from a Java environment.
2. The code is not organized in folders, even for repositories or services, since you were using that pattern. 

Open Questions
---
1. You mentioned you were awaiting containerization at your interview, why didn't you finally do it before submitting?
