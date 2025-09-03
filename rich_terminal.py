from rich.console import Console
from rich.table import Table


def tasks_table(tasks):
    console = Console()
    table = Table(title="Tasks")

    table.add_column("ID", justify="right")
    table.add_column("Description")
    table.add_column("Priority")
    table.add_column("Status")
    table.add_column("Created at")

    for task_id, info in tasks.items():
        table.add_row(
            task_id,
            info["description"],
            info["priority"],
            info["status"],
            info["created_at"],
        )

    console.print(table)
