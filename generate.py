import random


def main():
    print("Printing some random mounting")
    
    randomN = 2
    
    for i in range(99):
        randomN = random.randint(randomN - 2, randomN + 2)
        print_slach(randomN)




def print_slach(randomNumber):
    for i in range(randomNumber):
        print("#" , end='')
    print()


main()
