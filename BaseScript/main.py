import Levenshtein

types = {
    "Интеллектуальный": "1001",
    "Социальный": "0110",
    "Конвенциальный": "1011",
    "Истероидный": "0000",
    "Гипертимный": "1110"
}

user_ans = "1101"

min_distance = float('inf')

for type in types.keys():
    string = types[type]
    distance = Levenshtein.distance(user_ans, string)
    if distance < min_distance:
        min_distance = distance
        best_match = string
        best_type = type

print(best_match, best_type)