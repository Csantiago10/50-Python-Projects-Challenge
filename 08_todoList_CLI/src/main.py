import storage as st
import task_manager as tm


def main():
    tasks_list = st.load_tasks()
    while True:
        print("\nMenu:")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")
        option = input("Seleccione una opción: ")

        if option == "1":
            tm.show_tasks(tasks_list)
        elif option == "2":
            description = input("Ingrese la descripción de la tarea: ")
            tm.add_task(tasks_list, description)
        elif option == "3":
            if not tasks_list:
                print("No hay tareas para completar.")
                continue
            try:
                index = (
                    int(
                        input(
                            "Ingrese el índice de la tarea a marcar como completada: "
                        )
                    )
                    - 1
                )
                if 0 <= index < len(tasks_list):
                    tm.task_complete(tasks_list, index)
                else:
                    print("Índice de tarea no válido.")
            except ValueError:
                print("Error: Por favor ingrese un número válido.")
        elif option == "4":
            if not tasks_list:
                print("No hay tareas para eliminar.")
                continue
            try:
                index = int(input("Ingrese el índice de la tarea a eliminar: ")) - 1
                if 0 <= index < len(tasks_list):
                    tm.task_delete(tasks_list, index)
                else:
                    print("Índice de tarea no válido.")
            except ValueError:
                print("Error: Por favor ingrese un número válido.")
        elif option == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")


if __name__ == "__main__":
    main()
