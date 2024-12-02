import uuid


class Task:
    def __init__(self, title: str, description: str, category: str, due_date: str, priority: str,
                 status: str = "не выполнено", task_id: str = None):
        self.id = task_id or str(uuid.uuid4())  # Уникальный идентификатор
        self.title = title  # Название
        self.description = description  # Описание
        self.category = category  # Категория
        self.due_date = due_date  # Срок выполнения
        self.priority = priority  # Приоритет
        self.status = status  # Статус (выполнено/не выполнено)

    def mark_completed(self):
        """Отметить задачу как выполненную."""
        self.status = "выполнено"

    def update(self, title=None, description=None, category=None, due_date=None, priority=None):
        """Обновить поля задачи."""
        if title:
            self.title = title
        if description:
            self.description = description
        if category:
            self.category = category
        if due_date:
            self.due_date = due_date
        if priority:
            self.priority = priority

    def to_dict(self):
        """Преобразовать задачу в словарь для сохранения."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "due_date": self.due_date,
            "priority": self.priority,
            "status": self.status
        }

    @staticmethod
    def from_dict(data: dict):
        """Создать задачу из словаря."""
        return Task(
            title=data["title"],
            description=data["description"],
            category=data["category"],
            due_date=data["due_date"],
            priority=data["priority"],
            status=data["status"],
            task_id=data["id"]
        )
