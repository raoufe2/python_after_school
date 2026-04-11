
def main():
    number = int(input("Enter your number "))
    if is_even(number):
        print("Even")
    else:
        print("odd")


def is_even(number):
    if number % 2 == 0:
        return True

    return False



main()



