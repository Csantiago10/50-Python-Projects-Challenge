# 📝 Project 08: Persistent Task Manager (To-Do CLI)

> **Status:** Completed ✅
> **Author:** Engineer Santiago Noreña
> **Stack:** Python 3.12, File I/O, Git

## 📋 Description
This project consists of a task management system (To-Do List) that operates from the console. Its main feature is **Data Persistence**, which allows saving and retrieving information from the hard drive, preventing tasks from being lost when the program is closed.

Unlike previous projects that used volatile memory, this project implements a primitive database using plain text files.

## 🚀 Technical Features
The development focused on file handling and data structuring:

*   **Persistence (File I/O):** Use of `open()`, `read()`, and `write()` to interact with a `tasks.txt` file hosted in the `docs/` folder.
*   **Manual Parsing:** Implementation of a custom serialization format (`description|status`) without relying on libraries like `json` or `csv`, to understand low-level logic.
*   **Layered Architecture:** Clear separation of responsibilities:
    *   `storage.py`: Data access layer (File handling).
    *   `task_manager.py`: Business logic (List and dictionary manipulation).
    *   `main.py`: Presentation layer (User interaction).
*   **Error Handling:** Exception control (`FileNotFoundError`) to automatically initialize the database if it does not exist.

## 📂 Project Structure

```text
08_TodoList_CLI/
├── docs/
│   ├── especificaciones.md       # Requirements and persistence logic
│   ├── pseudocodigo.txt          # Algorithm planning
│   └── tasks.txt                 # Database (ignored in git)
├── src/
│   ├── main.py                   # User Interface (Menu)
│   ├── storage.py                # Persistence Layer (I/O)
│   └── task_manager.py           # Business Logic (CRUD)
├── test/
│   └── test_task_manager.py      # Unit tests with Mocking
├── .gitignore
└── README.md                     # Technical documentation
```