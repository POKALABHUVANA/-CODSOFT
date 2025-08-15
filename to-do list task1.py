import tkinter as tk
from tkinter import messagebox
tasks = []
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("warning", "Please enter a task!")
def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        tasks.pop(selected)
        update_listbox()
    except IndexError:
        messagebox.showwarning("warning","Please select a task to delete!")
def update_listbox():
    task_listbox.delete(0,tk.END)
    for task in tasks:
        task_listbox.insert(tk.END,task)
root = tk.Tk()
root.title("To-Do Lists")
task_entry = tk.Entry = tk.Entry(root,width=40)
task_entry.pack(pady=10)
add_btn = tk.Button(root,text="Add Task", command=add_task)
add_btn.pack(pady=10)
delete_btn = tk.Button(root, text="Delete Task", command=delete_task)
delete_btn.pack(pady=5)
task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)
root.mainloop()
