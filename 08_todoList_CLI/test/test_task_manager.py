import unittest
from unittest.mock import patch
import sys
import os

# Agregar la carpeta 'src' al path del sistema para que las importaciones funcionen
# Esto permite que 'import storage' dentro de task_manager no falle.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from task_manager import add_task, task_delete, task_complete


class TestTaskManager(unittest.TestCase):
    """
    Unit tests for the Task Manager (Project 08).
    Uses @patch to mock the storage layer and avoid writing
    to the real hard drive during tests.
    """

    def setUp(self):
        # Runs before each test: Reset the list
        self.tasks = []

    @patch("task_manager.st.save_tasks")
    def test_add_task(self, mock_save):
        """
        Test: Add a task.
        Verifies that the task is added to the in-memory list and save is called.
        """
        description = "Aprender Mocking"

        # Execute the function to test
        add_task(self.tasks, description)

        # Validations (Asserts)
        self.assertEqual(len(self.tasks), 1, "The list should have 1 element")
        self.assertEqual(self.tasks[0]["descripcion"], description)
        self.assertEqual(self.tasks[0]["estado"], "pendiente")

        # Verify that save was attempted (Mock)
        mock_save.assert_called_once_with(self.tasks)

    @patch("task_manager.st.save_tasks")
    def test_delete_task(self, mock_save):
        """
        Test: Delete a task.
        Verifies that the element is correctly removed by its index.
        """
        # Pre-condition: List with data
        self.tasks = [
            {"descripcion": "Tarea 1", "estado": "pendiente"},
            {"descripcion": "Tarea 2", "estado": "completada"},
        ]

        # Action: Delete the first task (index 0)
        task_delete(self.tasks, 0)

        # Validaciones
        self.assertEqual(len(self.tasks), 1, "The list should have 1 remaining element")
        self.assertEqual(
            self.tasks[0]["descripcion"], "Tarea 2", "Task 2 should remain"
        )

        # Verify persistence
        mock_save.assert_called_once_with(self.tasks)


if __name__ == "__main__":
    unittest.main()
