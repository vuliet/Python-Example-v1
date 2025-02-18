tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Đã thêm: {task}")

def show_tasks():
    print("\nDanh sách công việc:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

while True:
    action = input("\nNhập 'add' để thêm, 'show' để xem, 'exit' để thoát: ")
    if action == "add":
        task = input("Nhập công việc: ")
        add_task(task)
    elif action == "show":
        show_tasks()
    elif action == "exit":
        break
    else:
        print("Lệnh không hợp lệ!")
