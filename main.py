import random

from quotes import quotes

#app idea to give a quote depening on the type of genre selected by user,
#could be philosophical, about love, sadness, existentialism, etc.

def genre_of_quote():
    quote=random.choice(quotes)
    