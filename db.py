import os
import sqlite3

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'db.sqlite3')


def db_connect(db_path=DEFAULT_PATH):
    con = sqlite3.connect(db_path)
    return con

con = db_connect()
cur = con.cursor()

tasks_sql = """
CREATE TABLE IF NOT EXISTS tasks (
    id integer PRIMARY KEY,
    task_name text NOT NULL
)
"""
cur.execute(tasks_sql)

def new_task(task):
    query = "INSERT INTO tasks VALUES (NULL, ?)"
    cur.execute(query, (task,))
    con.commit()
    print(f"Adding task '{task}'")
    return cur.lastrowid

def all_tasks():
    cur.execute("SELECT id, task_name FROM tasks")
    return cur.fetchall()

def delete_task(id):
    query = "DELETE FROM tasks WHERE id=?"
    cur.execute(query, (id,))
    con.commit()
    print(f"Deleting task '{id}'")

if __name__ == "__main__":
    form_result = [f"{id:<5}{name}" for id, name in all_tasks()]
    id, name = "ID", "name"
    print("\n".join([f"{id:<5}{name}"] + form_result))
    con.close()
