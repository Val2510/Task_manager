from datetime import datetime
from task import Task
from task_manager import TaskManager


def validate_date(input_text: str) -> str:
    """Проверка и ввод корректной даты."""
    while True:
        value = input(input_text).strip()
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except ValueError:
            print("Неправильный формат даты. Используйте формат ГГГГ-ММ-ДД.")


def validate_priority(input_text: str) -> str:
    """Проверка корректности ввода приоритета."""
    valid_priorities = {"низкий", "средний", "высокий"}
    while True:
        value = input(input_text).strip().lower()
        if value in valid_priorities:
            return value
        print("Приоритет должен быть: низкий, средний или высокий. Попробуйте снова.")


def main():
    task_manager = TaskManager()
    file_path = "tasks.json"
    task_manager.load_from_file(file_path)

    while True:
        print("\nМеню:")
        print("1. Просмотреть задачи")
        print("2. Добавить задачу")
        print("3. Редактировать задачу")
        print("4. Отметить задачу как выполненную")
        print("5. Удалить задачу")
        print("6. Поиск задач")
        print("7. Выйти")
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            category = input("Введите категорию (оставьте пустым для всех задач): ").strip()
            tasks = task_manager.find_tasks_by_category(category) if category else None
            task_manager.view_tasks(tasks)
        elif choice == "2":
            title = input("Введите название задачи: ")
            description = input("Введите описание задачи: ")
            category = input("Введите категорию задачи: ")
            due_date = validate_date("Введите срок выполнения (гггг-мм-дд): ")
            priority = validate_priority("Введите приоритет (низкий, средний, высокий): ")
            task = Task(title, description, category, due_date, priority)
            task_manager.add_task(task)
            task_manager.save_to_file(file_path)
            print("Задача добавлена!")
        elif choice == "3":
            task_id = input("Введите ID задачи для редактирования: ")
            task = task_manager.find_task_by_id(task_id)
            if not task:
                print("Задача не найдена.")
                continue
            print("Оставьте поле пустым, если не хотите изменять.")
            title = input(f"Название ({task.title}): ") or None
            description = input(f"Описание ({task.description}): ") or None
            category = input(f"Категория ({task.category}): ") or None
            due_date = input(f"Срок выполнения ({task.due_date}): ")
            if due_date:
                due_date = validate_date("Введите новую дату (гггг-мм-дд): ")
            priority = input(f"Приоритет ({task.priority}): ") or None
            task.update(title, description, category, due_date, priority)
            print("Задача обновлена!")
        elif choice == "4":
            task_id = input("Введите ID задачи для отметки как выполненной: ")
            task = task_manager.find_task_by_id(task_id)
            if task:
                task.mark_completed()
                print("Задача отмечена как выполненная!")
            else:
                print("Задача не найдена.")
        elif choice == "5":
            task_id = input("Введите ID задачи для удаления: ")
            task_manager.delete_task(task_id)
            print("Задача удалена!")
        elif choice == "6":
            keyword = input("Введите ключевое слово, категорию или статус (выполнено/не выполнено): ").strip()
            results = task_manager.search_tasks(keyword)
            task_manager.view_tasks(results)
        elif choice == "7":
            task_manager.save_to_file(file_path)
            print("Изменения сохранены. Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
