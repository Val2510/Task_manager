import json
from task import Task


class TaskManager:
    def __init__(self):
        self.tasks = []  # Список задач

    def load_from_file(self, file_path: str):
        """Загрузить задачи из файла JSON."""
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                tasks_data = json.load(file)
                self.tasks = [Task.from_dict(task) for task in tasks_data]
        except FileNotFoundError:
            self.tasks = []
        except json.JSONDecodeError:
            print("Ошибка чтения файла. Данные повреждены.")
            self.tasks = []

    def save_to_file(self, file_path: str):
        """Сохранить задачи в файл JSON."""
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump([task.to_dict() for task in self.tasks], file, indent=4, ensure_ascii=False)
            print(f"Данные успешно сохранены в файл: {file_path}")
        except Exception as e:
            print(f"Ошибка при сохранении файла: {e}")

    def add_task(self, task: Task):
        """Добавить задачу."""
        self.tasks.append(task)

    def find_task_by_id(self, task_id: str):
        """Найти задачу по ID."""
        return next((task for task in self.tasks if task.id == task_id), None)

    def delete_task(self, task_id: str):
        """Удалить задачу по ID."""
        self.tasks = [task for task in self.tasks if task.id != task_id]

    def find_tasks_by_category(self, category: str):
        """Найти задачи по категории."""
        return [task for task in self.tasks if task.category == category]

    def search_tasks(self, keyword: str):
        """Поиск задач по ключевому слову."""
        keyword = keyword.lower()
        return [
            task for task in self.tasks
            if keyword in task.title.lower()
            or keyword in task.description.lower()
            or keyword in task.category.lower()
            or keyword == task.status.lower()  # Проверка на статус
        ]

    def view_tasks(self, tasks=None):
        """Просмотр задач."""
        tasks = tasks or self.tasks
        if not tasks:
            print("Нет задач для отображения.")
            return
        for task in tasks:
            print(f"\nID: {task.id}")
            print(f"Название: {task.title}")
            print(f"Описание: {task.description}")
            print(f"Категория: {task.category}")
            print(f"Срок выполнения: {task.due_date}")
            print(f"Приоритет: {task.priority}")
            print(f"Статус: {task.status}")
            print("-" * 40)
