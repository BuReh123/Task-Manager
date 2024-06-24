from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, name, description, due_date):
        if name in self.tasks:
            return f"Task with name '{name}' already exists."
        new_task = Task(name, description, due_date)
        self.tasks[name] = new_task
        return f"Task '{name}' added with due date {due_date}"

    def delete_task(self, task_name):
        if task_name in self.tasks:
            del self.tasks[task_name]
            return f"Task '{task_name}' has been deleted."
        return f"Task '{task_name}' not found."

    def view_tasks(self):
        if not self.tasks:
            return "No tasks available."
        return "\n".join([str(task) for task in self.tasks.values()])

    def clear_tasks(self):
        self.tasks.clear()
        return "All tasks cleared."
