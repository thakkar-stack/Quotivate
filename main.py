import random
import quotes

#app idea to give a quote depening on the type of genre selected by user,
#could be philosophical, about love, sadness, existentialism, etc.

def main():
    whichGenre()


def whichGenre():
    genre = input('Which genre of quote would you like?: Motivational(m), Philosophical(p), Love(l)?:' )
    if genre == ('m'):
        print(random.choice(quotes.motivational))
    elif genre == ('p'):
        print(random.choice(quotes.philosophical))
    elif genre == ('l'):
        print(random.choice(quotes.love))
        
main()