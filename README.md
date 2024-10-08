# ToDoGenius

ToDoGenius is a simple and intuitive web-based task management application built using HTML, CSS, Bootstrap, jQuery, and Flask with SQLite as the backend database. The app allows users to create, update, and delete tasks while providing filtering and sorting functionality for better task management.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [License](#license)

## Features

- Task Creation: Add new tasks with descriptions, due dates, and status.
- Task Filtering: Filter tasks based on their status (Todo, In-progress, Complete).
- Task Sorting: Sort tasks alphabetically or by due date.
- Task Editing: Update task details including description, status, and due date.
- Task Deletion: Delete tasks when they are no longer needed.

## Technologies

- Frontend:
  - HTML
  - CSS (Bootstrap 4.6.2)
  - Font Awesome
  - jQuery

-  Backend:
  - Flask
  - SQLite

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- Flask
- SQLite

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/ToDoGenius.git
    ```

2. Navigate to the project directory:

    ```bash
    cd ToDoGenius
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:

    ```bash
    python app.py
    ```

5. Open your browser and navigate to `http://localhost:5000`.

## Usage

- Add Task: Enter the task description, select a due date, and choose a status from the dropdown menu. Click the "Add" button to add the task to your list.

- Edit Task: Click the pencil icon next to the task you want to edit. Update the task's details in the modal that appears, and click "Update" to save changes.

- Delete Task: Click the trash icon next to the task you want to delete.

- Filter Tasks: Use the filter dropdown to view tasks by their status (Todo, In-progress, Complete).

- Sort Tasks: Use the sort dropdown to arrange tasks alphabetically or by due date.

## API Endpoints

- Add Task: `POST /addTask`
  - Parameters: `taskDate`, `taskDesc`, `taskStatus`

- Delete Task: `POST /deleteTask`
  - Parameters: `id`

- Update Task: `POST /updateTask`
  - Parameters: `id`, `Desc`, `status`, `date`

