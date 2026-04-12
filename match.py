name = input("Enter your name")


match name:
    case "RAOUF":
        print("find raouf name")
    case "cherifa" | "ahlam":
        print("Love")
    case _:
        print("Nothing found")
