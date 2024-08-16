import tkinter as tk

def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        pass

def clear_tasks():
    task_listbox.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List By Yash Singhal")

# Entry widget
task_entry = tk.Entry(root, width=40,bg="White")
task_entry.pack(pady=10)

# Add Task Button
add_task_btn = tk.Button(root, text="Add Task", command=add_task,bg="orange")
add_task_btn.pack(pady=5)

# Listbox to display tasks
task_listbox = tk.Listbox(root, width=50, height=10,bg="Grey")
task_listbox.pack(pady=10)

# Delete Task Button
delete_task_btn = tk.Button(root, text="Delete Task", command=delete_task,bg="orange")
delete_task_btn.pack(pady=5)

# Clear All Tasks Button
clear_tasks_btn = tk.Button(root, text="Clear All Tasks", command=clear_tasks,bg="orange")
clear_tasks_btn.pack(pady=5)

root.mainloop()