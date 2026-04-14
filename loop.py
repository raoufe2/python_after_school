
def print_n_times(n , message="NULL"):
    for i in range(n):
        print(message)

def print_and_break(n):
    
    for i in range(9999):
        if i == n:
            print("[BREAK]")
            break
    
        print("PRINT AND BREAK UNTIL USERE INPUT !")

def main():
    print_n_times(12)

    user_input = int(input("Please enter a number: "))
    print_and_break(user_input)
    

    for _ in ["raouf" , "cherifa" , "madina"]:
        print("hi")


main()
