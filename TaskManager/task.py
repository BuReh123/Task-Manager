class Task:
    """ Keeps track of current task and the name, able to output task and such"""
    def __init__(self, name, description, due_date):
        self.name = name
        self.description = description
        self.due_date = due_date
    
    def __str__(self):
        return f"{self.name}: {self.description} (Due: {self.due_date})"
