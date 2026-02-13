import os

# Define the absolute path to the tasks.txt file in the docs folder
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "docs", "tasks.txt")


def load_tasks():
    
    
    """
    Loads the tasks from the tasks.txt file and returns them as a list of dictionaries.
    If the file does not exist, it returns an empty list.
    """

    try:
        with open(DB_PATH, "r") as file:
            tasks_list = []
            for line in file:
                if line.strip():
                    description, status = line.strip().split("|")
                    tasks_list.append({"descripcion": description, "estado": status})
            return tasks_list
    except FileNotFoundError:
        return []


def save_tasks(tasks_list: list):
    """
    Docstring for save_tasks
    
    :param tasks_list: Description
    :type tasks_list: list
    """
    with open(DB_PATH, "w") as file:
        for task in tasks_list:
            file.write(f"{task['descripcion']}|{task['estado']}\n")
