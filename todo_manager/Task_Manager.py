Tasks = []
while True:
    Menu = input("Здравствуйте. Введите, пожалуйста, номер действия (1-4):\n1.Показать все задачи:\n 2.Добавить задачу:\n 3.Удалить задачу:\n 4.Выход:\n")
    if  Menu == "1":
        if not Tasks:
            print("Ваш список пуст!")
        else:
            print(f"\nВсе ваши задачи:")
            for number, task in enumerate(Tasks, 1):
                print(f"{number}. {task}")
    elif Menu == "2":
        New_Tasks = input("Введите название задачи которую хотите добавить: ")
        Tasks.append(New_Tasks)
        print("Задача добавлена!")
    elif Menu == "3":
        Delete_Tasks = input("Введите название задачи которую хотите удалить: ")
        Tasks.remove(Delete_Tasks)
        print("Задача удалена!")
    elif Menu == "4":
        with open("main.txt", "a", encoding="utf-8") as file:
            for task in Tasks:
                file.write(task + "\n")
        print("Ваши задачи сохранены! Всего доброго!")
        break 



