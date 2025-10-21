todos = []

while True:
    command = input("Type add, show, or quit: ")

    if command == "add":
        task = input("Enter a task: ")
        todos.append(task)
        print("Task added!")

    elif command == "show":
        print("Your To-Do List:")
        for todo in todos:
            print("- " + todo)

    elif command == "quit":
        print("Goodbye!")
        break

    else:
        print("Sorry, I didn’t understand that.")