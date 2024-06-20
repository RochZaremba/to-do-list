from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import datetime
import os
import subprocess

app = Flask(__name__)

# Function to create a new database and table if they don't exist
def initialize_database():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             task TEXT NOT NULL,
             due_date TEXT,
             completed INTEGER DEFAULT 0)''')
    conn.commit()
    conn.close()

# Function to add a new task to the database
def add_task(task, due_date=None):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    if due_date is None:
        due_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    c.execute("INSERT INTO tasks (task, due_date) VALUES (?, ?)", (task, due_date))
    conn.commit()
    conn.close()

# Function to delete a task from the database
def delete_task(task_id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()
    
# Function to view  tasks in the database
def view_tasks():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks WHERE completed=0")
    tasks = c.fetchall()
    conn.close()
    return tasks

def view_tasks_complited():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks WHERE completed=1")
    tasks = c.fetchall()
    conn.close()
    return tasks

# Function to update a task's details (task or due date)
def update_task(task_id, task=None, due_date=None):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    if task:
        c.execute("UPDATE tasks SET task=? WHERE id=?", (task, task_id))
    if due_date:
        if due_date.lower() == 'now':
            due_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        c.execute("UPDATE tasks SET due_date=? WHERE id=?", (due_date, task_id))
    conn.commit()
    conn.close()

# Function to mark a task as completed
def complete_task(task_id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("UPDATE tasks SET completed=? WHERE id=?", (1, task_id))
    conn.commit()
    conn.close()

# Initialize the database
initialize_database()

# Route to display tasks
@app.route('/')
def index():
    tasks = view_tasks()
    completed_tasks = view_tasks_complited() 
    return render_template('index.html', tasks=tasks, completed_tasks=completed_tasks)

# Route to add new task
@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    due_date = request.form['due_date']
    add_task(task, due_date)
    return redirect(url_for('index'))

# Route to update task
@app.route('/update/<int:task_id>', methods=['POST'])
def update(task_id):
    task = request.form['task']
    due_date = request.form['due_date']

    update_task(task_id, task, due_date,time_left)
    return redirect(url_for('index'))

# Route to delete task
@app.route('/delete/<int:task_id>', methods=['POST'])
def delete(task_id):
    delete_task(task_id)
    return redirect(url_for('index'))


# Route to mark task as completed
@app.route('/complete/<int:task_id>', methods=['POST'])
def complete(task_id):
    complete_task(task_id)
    print(view_tasks())
    return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.run(debug=True)




