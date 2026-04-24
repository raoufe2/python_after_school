def main():
    x = get_int("print the number of x: ")
    print(f"The value of x is {x}")



def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x
        except ValueError:
            pass


main()
