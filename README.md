Task-Organizer

Task-Organizer is a robust task management application that simplifies productivity with visually appealing task organization, sections for task separation, and integrated reminders for tasks. Built with modern web technologies, this application supports seamless communication between the frontend and backend while delivering efficient task management features.
Features

    Task Management
        Create, update, delete, and manage tasks efficiently.
        Mark tasks as completed with visual indicators for enhanced task tracking.

    Sections for Task Segmentation
        Organize tasks into sections for better categorization and management.

    Reminders
        Add reminders to tasks for timely notifications and improved productivity.

    Robust API Support
        Expanded and efficient endpoints for seamless frontend-backend communication.
        Enhanced data management to improve system performance.

Technologies Used

    Frontend: HTML, CSS, JavaScript
    Backend: Django, Django REST Framework
    Database: MySQL
    Containerization: Docker

Installation
Prerequisites

    Python 3.x
    Docker

Steps to Set Up Locally

    Clone the Repository

git clone https://github.com/ashcode002x/Task-Organizer/
cd Task-Organizer

Set Up Backend

    Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run migrations:

    python manage.py migrate


Run with Docker

    Build and start the application:

    docker-compose up --build

Run Without Docker

    Start the backend server:

        python manage.py runserver

        Access the application at http://127.0.0.1:8000.

Usage

    Create an Account
    Sign up or log in to access your personalized task dashboard.
    For development preview use aashi for login and 1234 for password 
    Add Tasks
        Create tasks under specific sections.
        Add reminders for important deadlines.

    Track Progress
        Mark tasks as completed to keep your task list updated.
        Use visual indicators for progress tracking.

Contribution

Contributions are welcome! Feel free to fork the repository and submit pull requests.
License

This project is licensed under the MIT License.
