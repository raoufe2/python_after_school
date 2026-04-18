def main():
    while(True):
        print("Print the height and the width do you want to use for the square :")
        height = int(input("Height: "))
        width = int(input("width: "))

        print("Print the cube : ")

        print_square(height , width)
        
        #ask the user if he want to continue with the printing

        user_bool = input("Do you want to continue tab (yes)")

        if user_bool != "yes":
            break


def print_row(n):
    print("?" * n)

def print_square(height , width):
    for _ in range(height):
        for _ in range(width):
            print("#" , end="")
        print()


main()
