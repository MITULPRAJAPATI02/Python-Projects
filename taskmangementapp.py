def task():
    tasks = []
    print("----WELCOME TO THE TASK MANAGEMENT APP----")

    total_task = int(input("Enter the number of tasks you want to add: "))

    for i in range(total_task):
        task_name = input(f"Enter task {i+1}: ")
        tasks.append(task_name)

    print(f"Today's tasks are \n {tasks}")

    while True:
        operation = int(input("Enter 1-To add task\n 2-Update\n 3-Delete\n 4-View\n 5-Exit/stop "))
        if operation == 1:
            add = input("Enter task you want to add = ")
            tasks.append(add)
            print(f"Task {add} has been successfully added....")

        elif operation == 2:
            updated_val = input("Enter the task name you want to update = ")
            if updated_val in tasks:
                up = input("Enter new task = ")
                index = tasks.index(updated_val)
                tasks[index] = up
                print(f"Updated task {up}")
            else:
                print("Task not found.")

        elif operation == 3:
            del_val = input("Which task you want to delete = ")
            if del_val in tasks:
                tasks.remove(del_val)
                print(f"Task {del_val} has been deleted..")
            else:
                print("Task not found.")

        elif operation == 4:
            print(f"Total tasks = {tasks}")

        elif operation == 5:
            print("Closing the program.........")
            break
        else:
            print("Invalid input")

