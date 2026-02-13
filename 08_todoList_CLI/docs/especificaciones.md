# Specifications: Persistent Task Manager (Project 08)

## 1. Description
Task management system (To-Do List) operating from the command line (CLI). Unlike previous projects, this introduces the concept of **Data Persistence**, allowing information to be saved and retrieved from the hard drive so that tasks are not lost when the program is closed.

**Author:** Engineer Santiago Noreña
**Date:** 02/14/2026
**Status:** ✅ Completed

## 2. Functional Requirements
- **Main Menu:** Cyclic interface with the following options:
    1. View tasks.
    2. Add task.
    3. Mark task as completed.
    4. Delete task.
    5. Exit.
- **Visualization:** Tasks must visually display their index and status:
    - `[ ] 1. Buy milk` (Pending)
    - `[X] 2. Study Python` (Completed)
- **Automatic Persistence:**
    - On startup: Load existing tasks from `tasks.txt`.
    - On modification (Add/Delete/Complete): Save changes immediately to `tasks.txt`.

## 3. Technical Requirements (Architecture)
- **File Structure:**
    - `src/storage.py`: Module exclusively responsible for File I/O (Input/Output).
    - `src/task_manager.py`: Business logic (in-memory list manipulation).
    - `src/main.py`: User interface and main loop.
- **File Format (`tasks.txt`):**
    - Plain text file.
    - Custom separator: `|` (pipe).
    - Structure per line: `description|status`.
    - *Example:* `Buy bread|pendiente`
- **In-Memory Data Structure:**
    - List of dictionaries for key-based access.
    - `[{"descripcion": "...", "estado": "pendiente"}, ...]`

## 4. Persistence Logic (Parsing)
Libraries like `json` or `csv` will not be used for educational purposes. Parsing will be manual:

### Reading (`load_tasks`)
1. Open file in read mode (`'r'`).
2. Read line by line.
3. Use `.strip()` to remove newlines.
4. Use `.split('|')` to separate description and status.
5. **Error Handling:** If the file does not exist (`FileNotFoundError`), return an empty list without crashing the program.

### Writing (`save_tasks`)
1. Open file in write mode (`'w'`).
2. Iterate through the task list.
3. Format each task as an f-string: `f"{t['descripcion']}|{t['estado']}\n"`.
4. Write to the file.

## 5. Test Cases (QA)
| Action | Input | File State (`tasks.txt`) | Visual Result |
| :--- | :--- | :--- | :--- |
| **Start (No file)** | - | (Does not exist) | Empty list, creates file on save. |
| **Add** | "Study" | `Study|pendiente` | `[ ] 1. Study` |
| **Complete** | ID: 1 | `Study|completada` | `[X] 1. Study` |
| **Persistence** | (Restart App) | `Study|completada` | `[X] 1. Study` (Recovered) |
| **Delete** | ID: 1 | (Empty file) | Empty list. |

## 6. Version Control (Git)
- The `tasks.txt` file must be ignored by git to avoid uploading test tasks to the repository.
- Add `tasks.txt` to the `.gitignore` file.