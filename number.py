
try:
    x = int(input("Enter the value of x: "))
except ValueError:
    print("Please enter a number !!")
else:
    print(f"the value of x is {x}")
