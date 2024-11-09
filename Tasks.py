import tkinter as tk
from tkinter import ttk

class ToDoApp:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("To-Do List")

        # Create a list to store tasks
        self.task_list = []
        # Create a variable to hold the current task input
        self.task_var = tk.StringVar()

        # Create a text entry field for inputting tasks
        self.task_entry = ttk.Entry(root, textvariable=self.task_var)
        self.task_entry.pack(pady=10)

        # Create a button to add tasks to the list
        self.add_button = ttk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        # Create a listbox to display tasks
        self.task_listbox = tk.Listbox(root)
        self.task_listbox.pack(fill=tk.BOTH, expand=True)

        # Create a button to delete tasks from the list
        self.delete_button = ttk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Create a button to edit tasks in the list
        self.edit_button = ttk.Button(root, text="Edit Task", command=self.edit_task)
        self.edit_button.pack(pady=5)

    def add_task(self):
        # Get the task from the entry field
        task = self.task_var.get()
        # If the task is not empty, add it to the list and listbox
        if task:
            self.task_list.append(task)
            self.task_listbox.insert(tk.END, task)
            # Clear the entry field
            self.task_var.set("")

    def delete_task(self):
        # Get the index of the selected task
        selected_index = self.task_listbox.curselection()
        # If a task is selected, delete it from the list and listbox
        if selected_index:
            self.task_listbox.delete(selected_index)
            del self.task_list[selected_index[0]]

    def edit_task(self):
        # Get the index of the selected task
        selected_index = self.task_listbox.curselection()
        # If a task is selected, prompt the user for a new task
        if selected_index:
            old_task = self.task_list[selected_index[0]]
            new_task = tk.simpledialog.askstring("Edit Task", f"Enter new task for '{old_task}':")
            # If a new task is provided, update the list and listbox
            if new_task:
                self.task_list[selected_index[0]] = new_task
                self.task_listbox.delete(selected_index)
                self.task_listbox.insert(selected_index[0], new_task)

if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    # Create an instance of the ToDoApp class
    app = ToDoApp(root)
    # Start the main event loop
    root.mainloop()