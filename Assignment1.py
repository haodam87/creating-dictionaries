tasks = [] 
def add():
    while True: 
        title = input("\nEnter name of your task: ")
        priority = input("\nEnter priority: (low, med, high): ")
        task = {"title": title, "priority": priority}

        tasks.append(task)

        choice = input("\nEnter q to quit or any key to continue: ")
        if choice == "q": 
            break 


def view():
    for index in range(0, len(tasks)):
        task = tasks[index]
        print(f"\n{index +1} - {task['title']} : {task['priority']} priority")

def delete():
    while True:
        delete_task =input("\nSelect a task number to delete:")
        if delete_task == "q":
            break
        else:
            del tasks[(int(delete_task))-1]
            break

while True: 
    menu = input("\nPress 1 to add task \nPress 2 to delete task \nPress 3 to view all tasks \nPress q to quit \n:")

    if menu == "1":
        add()
    elif menu == "2":
        view()
        delete()
    elif menu == "3":
        view()
    elif menu ==  "q":
        break
    else:
        print("You have entered invalid option.")


# print(tasks)