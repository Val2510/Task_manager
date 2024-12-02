import pytest
from task import Task
from task_manager import TaskManager


@pytest.fixture
def sample_task_manager():
    """Фикстура для создания TaskManager с тестовыми данными."""
    manager = TaskManager()
    manager.add_task(Task(title="Сделать домашнее задание", description="Математика и программирование",
                          category="Учеба", due_date="2024-12-05", priority="высокий"))
    manager.add_task(Task(title="Купить продукты", description="Молоко, хлеб, сыр",
                          category="Личное", due_date="2024-12-03", priority="средний"))
    return manager


def test_add_task():
    """Тест функции добавления задачи."""
    manager = TaskManager()
    task = Task(title="Новая задача", description="Описание", category="Работа",
                due_date="2024-12-10", priority="средний")
    manager.add_task(task)

    assert len(manager.tasks) == 1
    assert manager.tasks[0].title == "Новая задача"
    assert manager.tasks[0].status == "не выполнено"


def test_mark_completed(sample_task_manager):
    """Тест отметки задачи как выполненной."""
    task = sample_task_manager.tasks[0]
    task.mark_completed()

    assert task.status == "выполнено"


def test_search_tasks(sample_task_manager):
    """Тест поиска задач."""
    results = sample_task_manager.search_tasks("Купить")
    assert len(results) == 1
    assert results[0].title == "Купить продукты"

    results = sample_task_manager.search_tasks("Учеба")
    assert len(results) == 1
    assert results[0].category == "Учеба"

    results = sample_task_manager.search_tasks("не выполнено")
    assert len(results) == 2


def test_delete_task(sample_task_manager):
    """Тест удаления задачи."""
    initial_count = len(sample_task_manager.tasks)
    task_to_delete = sample_task_manager.tasks[0]
    sample_task_manager.delete_task(task_to_delete.id)

    assert len(sample_task_manager.tasks) == initial_count - 1
    assert task_to_delete not in sample_task_manager.tasks
