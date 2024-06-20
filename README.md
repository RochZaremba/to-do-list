# To-Do App

This To-Do App allows users to manage their tasks efficiently. It provides functionality to add, view, and delete tasks, with an option to set due dates and countdown timers.

## Features

- **Add New Tasks**: Users can add new tasks with an optional due date.
- **View Tasks**: Active tasks and completed tasks are displayed separately.
- **Task Countdown**: Displays a countdown timer for tasks with due dates.
- **Mark Tasks as Complete**: Users can mark tasks as complete.
- **Delete Tasks**: Users can delete both active and completed tasks.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/todo-app.git
    ```
2. Navigate to the project directory:
    ```sh
    cd todo-app
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```sh
    python main.py
    ```
2. Open your web browser and navigate to:
    ```sh
    http://localhost:5000
    ```

## File Structure

- `main.py`: The main Python file that runs the Flask application.
- `templates/index.html`: The HTML template for the app's front end.
- `static/styles.css`: The CSS file for styling the app (assuming you have a stylesheet in place).

## Main Files Description

### main.py

This file contains the Flask application code. It handles routing, form submissions, and task management logic.

### index.html

This file contains the HTML structure and JavaScript code for the countdown timer. It uses Jinja templating to dynamically display tasks and their respective due dates.

## Adding a New Task

1. Enter the task name in the "Task" field.
2. (Optional) Set a due date and time in the "Due Date" field.
3. Click the "Add Task" button.

## Marking a Task as Complete

1. Click the "Complete" button next to the task you want to mark as complete.

## Deleting a Task

1. Click the "Delete" button next to the task you want to delete.

## License

This project is licensed under the MIT License.

---

Feel free to customize this README to better fit your project's specifics and style.
