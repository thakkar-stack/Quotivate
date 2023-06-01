import random
import quotes

#app idea to give a quote depening on the type of genre selected by user,
#could be philosophical, about love, sadness, existentialism, etc.

def main():
    whichGenre()


def whichGenre():
    genre = input('Which genre of quote would you like?:')
    if genre == (quotes.genres[0]):
        print(random.choice(quotes.motivational))
    elif genre == (quotes.genres[1]):
        print(random.choice(quotes.philosophical))
        
main()