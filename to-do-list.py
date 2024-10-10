import json
import os


TODO_FILE = "todo_list.json"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    task = input("Enter a new task: ")
    priority = input("Enter priority (high, medium, low): ").lower()
    tasks.append({"task": task, "priority": priority, "done": False})
    print(f"Task '{task}' added.")

def list_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
        return
    for idx, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Pending"
        print(f"{idx}. {task['task']} [{task['priority']}] - {status}")

def mark_task_done(tasks):
    list_tasks(tasks)
    task_num = int(input("Enter task number to mark as done: "))
    if 0 < task_num <= len(tasks):
        tasks[task_num - 1]["done"] = True
        print(f"Task '{tasks[task_num - 1]['task']}' marked as done.")
    else:
        print("Invalid task number.")

def remove_task(tasks):
    list_tasks(tasks)
    task_num = int(input("Enter task number to remove: "))
    if 0 < task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        print(f"Task '{removed_task['task']}' removed.")
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List ---")
        print("1. Add a task")
        print("2. List tasks")
        print("3. Mark task as done")
        print("4. Remove a task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            list_tasks(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()

