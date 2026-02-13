import storage as st


def add_task(tasks_list: list, description: str):
    """Adds a new task to the list and saves it to storage."""
    tasks_list.append({"descripcion": description, "estado": "pendiente"})
    st.save_tasks(tasks_list)
    print("Tarea agregada con éxito.")


def task_complete(tasks_list: list, index: int):
    """Marks a task as completed based on its index and updates storage."""
    tasks_list[index]["estado"] = "completada"
    st.save_tasks(tasks_list)
    print("Tarea marcada como completada.")


def task_delete(tasks_list: list, index: int):
    """Removes a task from the list based on its index and updates storage."""
    tasks_list.pop(index)
    st.save_tasks(tasks_list)
    print("Tarea eliminada con éxito.")


def show_tasks(tasks_list: list):
    """Displays all tasks with their status and index."""
    print("\n" + "=" * 50)
    print("             Lista de tareas")
    print("=" * 50)

    if not tasks_list:
        print("\nNo hay tareas registradas.")
        return

    for i, task in enumerate(tasks_list, start=1):
        status = "[X]" if task["estado"] == "completada" else "[ ]"
        print(f"{status} {i}. {task['descripcion']}")
