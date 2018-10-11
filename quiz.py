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

def add_a_question():
    question = input("enter a question: ")
    answer = input("ok then tell me, " + question.lower() + ": ")
    
    with open("questions.txt", "a") as f:
        line = question + "|" + answer + "\n"
        f.write(line) 
    


while True:
    option = show_menu()
    
    if option == "1":
        print("you picked run quiz")
    
    if option == "2":
        add_a_question()
    
    if option == "3":
        break

