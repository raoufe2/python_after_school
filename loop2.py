def main():
    n = int(input("Enter n : "))
    word = input("Enter the word to print n times")
    print_word(n , word)


def print_word(n , word):
    if n <= 0 or word == "":
        print("N is negative or you word is empty")
        return
    
    for _ in range(n):
        print(word)






main()
