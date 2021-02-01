import tkinter as tk
from datetime import date
import db



class Task:
    def __init__(self, id, text):
        self.id = id
        self.label = tk.Label(master=task_frame, text=text)
        self.button = tk.Button(master=task_frame, text="Finish", command=self.finish)
        self.label.pack()
        self.button.pack()

    def finish(self):
        db.delete_task(self.id)
        self.button.destroy()
        self.label.destroy()

def make_task():
    task = new_task.get()
    id = db.new_task(task)
    tasks.append(Task(id, task))
    new_task.delete(0, 'end')

window = tk.Tk()


title = tk.Label(text=f"Todo for {date.today()}")
title.pack()
task_frame = tk.Frame()
task_frame.pack()

tasks = [Task(id, task) for id, task in db.all_tasks()]

new_task = tk.Entry()
new_task.pack()
new_btn = tk.Button(text="Add new task", command=make_task)
new_btn.pack()

window.mainloop()
