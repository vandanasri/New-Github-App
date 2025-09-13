import json
import os

TODO_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task_description):
    tasks = load_tasks()
    tasks.append({"task": task_description, "done": False})
    save_tasks(tasks)
    print(f"✅ Added: {task_description}")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📝 No tasks found.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. {status} {task['task']}")

def mark_done(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        print(f"✔️ Marked task #{task_number} as done.")
    else:
        print("⚠️ Invalid task number.")

def delete_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"🗑️ Deleted task: {removed['task']}")
    else:
        print("⚠️ Invalid task number.")

def menu():
    while True:
        print("\n📋 To-Do App Menu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            task = input("Enter the task description: ")
            add_task(task)
        elif choice == "3":
            try:
                num = int(input("Enter task number to mark as done: "))
                mark_done(num)
            except ValueError:
                print("⚠️ Please enter a valid number.")
        elif choice == "4":
            try:
                num = int(input("Enter task number to delete: "))
                delete_task(num)
            except ValueError:
                print("⚠️ Please enter a valid number.")
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
