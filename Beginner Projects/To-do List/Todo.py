# A list where you can add, remove and view tasks. Store tasks in memory or save/load from a file.
# Hints: Lists, string and File Handling
# Terminal Based

# COMPLETED BASIC FUNCTIONALITY

todolist = []

print("Enter 'add' to add a task.")
print("Enter 'del' to remove a task.")
print("Enter 'view' to view a task.")
print("Enter 'save' to save a tasks.")
print("Enter 'done' to complete a task.")
print("Enter 'load' to view saved tasks.")
print("Enter 'quit' to quit the program.")

while True:
    userinput = input("Enter task to be performed('add', 'del', 'view', 'save', 'done', 'load', 'quit'): ")
    if userinput.lower() == "add":
        while True:
            addtodo = input("Add a task(or 'quit'): ")
            if addtodo.lower() == "quit":
                break
            else: 
                todolist.append(addtodo)
                print("Task Added.")
                print("Current List:",todolist)

    elif userinput.lower() == "del":
        print(todolist)
        for item in todolist:
            print(todolist.index(item)+1, "->", end=" ")
            print(item)
        todolist.pop(int(input("What task do you want to remove? "))-1)

    elif userinput.lower() == "view":
        print(f"The current Todo list looks like this: {todolist}")
        for item in todolist:
            print(todolist.index(item)+1, end=" ")
            print(item)

    elif userinput.lower() == "save":
        with open("todo.txt", "a") as file:
            file.write(str(todolist))
            file.write("\n")
        print("Successfully saved!")

    elif userinput.lower() == "done":
        print("Under Development!")

    elif userinput.lower() == "load":
        file = open("todo.txt", "r")
        content = file.read()
        print(content)
        file.close()

    elif userinput.lower() == "quit":
        break