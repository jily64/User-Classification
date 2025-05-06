import Levenshtein
import models

def check_user_exist(email):
    return True


def set_value_user(name, value, email):
    pass

def get_value_user(email, value):
    return value

def check_questionare(ans):
    types = {
        "Интеллектуальный": "1001",
        "Социальный": "0110",
        "Конвенциальный": "1011",
        "Истероидный": "0000",
        "Гипертимный": "1110"
    }

    user_ans = ans

    min_distance = float('inf')

    for type in types.keys():
        string = types[type]
        distance = Levenshtein.distance(user_ans, string)
        if distance < min_distance:
            min_distance = distance
            best_type = type

    return models.PsycoType(**{"matched": best_type})