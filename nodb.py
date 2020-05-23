todos = []

def insert_todo(todo):
    todos.append(todo)
    return "inserted"

while True:
    print("Select an option: 1. Insert Todo  2. Get all todos")
    option = input("option: ")
    if option == "1":
        todo = input("Enter todo: ")
        insert_todo(todo)
    elif option == "2":
        print("---------------------------\n")
        print("Your tasks")
        print("---------------------------\n")

        for t in todos:
            print(t)
            
        print("---------------------------\n")
    else:
        print("wrong option")
    

