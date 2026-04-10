def main():
    x = input("Enter the value of x : ")
    x = int(x)
    print("x squared is" , square(x))


def square(x=0):
    return pow(x , 2)


main()




