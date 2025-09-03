from datetime import datetime
import json
from constants import DEFAULT_STATUS, DEFAULT_PRIORITY
from rich_terminal import tasks_table


class Task:
    def __init__(
        self,
        id: int,
        description: str,
        priority: str = DEFAULT_PRIORITY,
        status: str = DEFAULT_STATUS,
    ) -> None:
        self.id = id
        self.description = description
        self.priority = priority
        self.status = status
        self.created_at = datetime.now().strftime("%X")

    def __iter__(self):
        return iter(
            (self.id, self.description, self.priority, self.status, self.created_at)
        )

    def to_dict(self) -> dict:
        return {
            "description": self.description,
            "priority": self.priority,
            "status": self.status,
            "created_at": self.created_at,
        }


class Task_Manager:
    def __init__(self) -> None:
        self.tasks: dict = {}

    def load_file_action(self, action: str, file_name: str = "task.json"):
        with open(file_name, action) as file:
            tasks = json.load(file)
        return tasks

    def dump_file_action(self, action: str, obj, file_name: str = "task.json") -> None:
        with open(file_name, action) as file:
            json.dump(obj, file, indent=4)

    def add_task(
        self,
        id: int,
        description: str,
        priority: str = DEFAULT_PRIORITY,
        status: str = DEFAULT_STATUS,
        file_name: str = "task.json",
    ):
        task = Task(id, description, priority, status)

        try:
            tasks = self.load_file_action("r")

        except (FileNotFoundError, json.JSONDecodeError):
            tasks = {}

        tasks[str(id)] = task.to_dict()

        self.dump_file_action("w", tasks, file_name)

        self.tasks = tasks

    def delete_task(self, id: int, file_name: str = "task.json") -> None:
        tasks = self.load_file_action("r", file_name)

        str_id: str = str(id)
        if str_id in tasks:
            del tasks[str_id]
            print(f"Task {id} deleted")
            self.dump_file_action("w", tasks, file_name)
            self.tasks = tasks
        else:
            print(f"Task {id} not found")

    def update_task(
        self,
        id: int,
        new_description: str,
        new_priority: str = DEFAULT_STATUS,
        new_status: str = DEFAULT_STATUS,
        file_name: str = "task.json",
    ) -> None:
        tasks = self.load_file_action("r")

        str_id: str = str(id)
        if str_id in tasks:
            old_created_at = tasks[str_id].get(
                "created_at", datetime.now().strftime("%X")
            )
            tasks[str_id] = {
                "description": new_description,
                "priority": new_priority,
                "status": new_status,
                "created_at": old_created_at,
            }

            self.dump_file_action("w", tasks, file_name)

            self.tasks = tasks
            print(f"Task {id} updated successfully")

        else:
            print("Task {id} not found")

    def view_tasks(self) -> None:
        tasks = self.load_file_action("r")
        tasks_table(tasks)


tasks_manager = Task_Manager()
