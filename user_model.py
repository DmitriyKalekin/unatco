

class UserModel:
    def __init__(self):
        self.chat_it = None
        self.db = {}

    def set_chat(self, chat_id):
        self.chat_it = chat_id


    def create_game(msg, chat_id):
        return {
            "state": {},
            "step": "start",
            "$": 10000,
            "day": 1,
            "candidates": [
                create_person(),
                create_person(),
                create_person()
            ],
            "deps": {
                "sci": [],
                "cops": [],
                "agents": [],
            }
        }

        

    def create_person(name=""):
        first_names = ["Feudor", "Boris", "Alex", "Mark", "JC"]
        second_names = ["Denton", "Fork", "Blade", "Ivanov", "Smith", "Volkov"]

        if not name:
            name = choice(first_names) + " " + choice(second_names)
        
        strenght = choice([2,4,5])
        agility = choice([3,4,5])
        intelligence = choice([1,2,4])

        return {
            "name": name,
            "s": strenght,
            "a": agility,
            "i": intelligence,
            "loc": "hq"
        }

