import os

import promts


def pick(file_path, data):
    import pickle
    with open(file_path, 'wb') as file:
        pickle.dump(data, file)


def unpick(file_path):
    import pickle
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
    return data


class Dark:

    def __init__(self, user_id):
        self.api_key = "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"

        self.user_id = user_id
        self.model = "gpt-3.5-turbo"
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }

        if not self.history_exists(self.user_id):
            self.new_history(self.user_id)

    def history_exists(self, filename):
        import os

        if filename not in os.listdir("history"):
            return False
        return True

    def new_history(self, filename, history=[]):
        if history == []:
            pick(f"history/{filename}", [
                {"role": "system", "content": promts.Dark.instructions}
            ])
        else:
            pick(f"history/{filename}", history)

    def generate(self, history=[]):
        import requests
        import json

        if len(history) >= 1:
            unpick_data = [{"role": "system", "content": promts.Dark.instructions}]
            for i in history:
                unpick_data.append(i)

        else:
            raise Exception("History is empty")

        data = {
            "model": self.model,
            "messages": unpick_data,
        }

        response = requests.post('https://api.openai.com/v1/chat/completions', headers=self.headers, data=json.dumps(data))
        response = eval(response.text.replace("null", "None"))
        return response

    def add_to_history(self, role, message):
        unpick_data = unpick(f"history/{self.user_id}")
        unpick_data.append({"role": role, "content": message})
        pick(f"history/{self.user_id}", unpick_data)

    @staticmethod
    def get_text_only(message):
        return message["choices"][0]["message"]["content"]


