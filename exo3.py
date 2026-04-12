def main():
    number = int(input("Enter your number "))
    if is_even(number):
        print("Even")
    else:
        print("odd")


    #check if number from 0 to 100 are permier or not

    for i in range(101):
        print(f"{i} est : {is_premier(i)}")

def is_even(number):
    if number % 2 == 0:
        return True

    return False


def is_pair(number):
    return (number % 2 == 0)

def is_premier(number):
    count = number - 1
    while count >= 2:
        if number % count == 0:
            return False

        count -= 1

    return True



main()



