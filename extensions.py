import json


class DataBase:
    def __init__(self):
        self.users = self.load_data("users.json")
        self.questions = self.load_data("questions.json")
        self.questions_count = len(self.questions)

    @staticmethod
    def load_data(file_name):
        try:
            with open(file_name, "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        return data

    @staticmethod
    def save_data(data, file_name):
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(data, file)

    def get_user(self, chat_id):
        for user in self.users:
            if user["chat_id"] == chat_id:
                return user
        user = {
            "chat_id": chat_id,
            "is_passing": False,
            "is_passed": False,
            "question_index": None,
            "answers": []
        }
        self.users.append(user)
        self.save_data(self.users, "users.json")
        return user

    def set_user(self, chat_id, update):
        for user in self.users:
            if user["chat_id"] == chat_id:
                user.update(update)
                self.save_data(self.users, "users.json")
                return

    def get_question(self, index):
        if 0 <= index < len(self.questions):
            return self.questions[index]
        return None

    @staticmethod
    def load_comparison(filename="comparison_animal.json"):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        return data

    @staticmethod
    def load_condition(filename="condition_animal.json"):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        return data
