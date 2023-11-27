prompt = "Enter a todo: "
action = "type add/show/remove/edit/exit: "

with open("todo.txt", 'r') as files:
    todo = files.readlines()

while True:
    user_action = input(action).strip().capitalize()

    match user_action:
        case 'Add' | 'New':
            todos = input(prompt) + "\n"

            todo.append(todos)

            with open("todo.txt", 'w') as file:
                file.writelines(todo)

        case 'Show' | 'Display':
            l1 = [i.strip('\n') for i in todo]

            for i, x in enumerate(l1):
                print(f"{i + 1}. {x}")

        case 'Remove' | 'Delete' | 'Complete':
            number = input("Enter number to delete: ")
            d = int(number) - 1
            todo.pop(d)

            with open("todo.txt", 'w') as file:
                file.writelines(todo)

        case 'Edit' | 'Change':
            number = input("Enter number to edit: ")
            e = int(number) - 1
            change = input("Enter a change: ")
            todo[e] = change + '\n'

            with open("todo.txt", 'w') as file:
                file.writelines(todo)

        case 'Exit' | 'End':
            break

        case default:
            print("Invalid Answer")
