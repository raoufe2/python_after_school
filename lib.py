from random import choice
from random import randrange
import random

def main():
    print("algorith for fliping a cois")
    x = choice(['head' , 'tail'])
    print(x)
    
    ##work with random.randrange(start , stop , step)

    randomNumber = randrange(0 , 100 , 10)
    print(f"Random Number from randm.randrange is: {randomNumber}")

    #work with random.randint(a, b)

    randomNumber = random.randint(100 , 1999)
    print(f"Random Number from random.randint is {randomNumber}")

main()
