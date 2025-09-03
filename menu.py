from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from task import tasks_manager
from constants import STATUS, PRIORITY


def menu():
    while True:
        action = inquirer.select(
            message="Select an action:",
            choices=[
                "Add a new task",
                "Remove a task",
                "View tasks",
                "Update a task",
                "Exit",
            ],
            vi_mode=True,
            default=None,
        ).execute()

        m_action: str = menu_action(action)
        if m_action == "Exit":
            break


def menu_action(action: str):
    if action == "Add a new task":
        id = inquirer.text("id: ").execute()
        description = inquirer.text("Task: ").execute()
        priority: PRIORITY = inquirer.select(
            message="priority: ",
            choices=["low", "medium", "high"],
            vi_mode=True,
        ).execute()
        status: STATUS = inquirer.select(
            message="Status: ",
            choices=["!completed", "in progress", "completed"],
            vi_mode=True,
        ).execute()

        tasks_manager.add_task(id, description, priority, status)
        tasks_manager.view_tasks()

    if action == "Remove a task":
        task_id = inquirer.text("Task id to delete: ").execute()
        tasks_manager.delete_task(task_id)

    if action == "Update a task":
        id = inquirer.text("Task id to update: ").execute()
        description = inquirer.text("Task: ").execute()
        priority: PRIORITY = inquirer.select(
            message="priority: ",
            choices=["low", "medium", "high"],
            vi_mode=True,
        ).execute()
        status: STATUS = inquirer.select(
            message="Status: ",
            choices=["!completed", "in progress", "completed"],
            vi_mode=True,
        ).execute()

        tasks_manager.update_task(id, description, priority, status)

    if action == "View tasks":
        tasks_manager.view_tasks()

    return action


if __name__ == "__main__":
    menu()
