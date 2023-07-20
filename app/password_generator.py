import random
from wordlists import adjectives, nouns, verbs, special_chars, numerals

def generate_password():
    adj = random.choice(adjectives)
    noun1 = random.choice(nouns)
    verb = random.choice(verbs)
    noun2 = random.choice(nouns)
    num = random.choice(numerals)
    char = random.choice(special_chars)
    password = f"{adj}{noun1}{verb}{noun2}{num}{char}"
    return password