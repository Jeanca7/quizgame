def show_menu():
    print("quiz game")
    print("-------------")
    print("")
    print("1. run quiz")
    print("2. enter a question")
    print("3. exit")
    print("")

    option = input("Enter Option: ")
    return option

while True:
    option = show_menu()
    if option == "3":
        break