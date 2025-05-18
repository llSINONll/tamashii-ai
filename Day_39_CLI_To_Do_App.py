'''
Let’s build a simple Python command-line Todo app with basic features like:

Adding tasks ✅

Viewing tasks 📋

Marking tasks as complete 🟩

Saving to a file 💾
1. Add Task
2. View Tasks
3. Mark Task as Done
4. Exit
Enter choice: 1
Enter task: Buy pencils
Task added!

Enter choice: 2
1. [❌] Buy pencils

'''
import os

FILENAME = "todo.txt"

def load_tasks():
    tasks = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                task, done = line.strip().split("||")
                tasks.append({"task": task, "done": done == "True"})
    return tasks

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(f"{task['task']}||{task['done']}\n")

def add_task(tasks):
    task_text = input("Enter task: ")
    tasks.append({"task": task_text, "done": False})
    print("✅ Task added!")

def view_tasks(tasks):
    if not tasks:
        print("📭 No tasks yet!")
        return
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. [{status}] {task['task']}")

def mark_done(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            print("🎉 Task marked as done!")
        else:
            print("Invalid number!")
    except ValueError:
        print("Enter a valid number!")

def main():
    tasks = load_tasks()
    while True:
        print("\n📝 Todo Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("📦 Tasks saved! Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
