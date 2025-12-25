# Student Management System

## Overview

The Student Management System is a Django-based REST API designed to facilitate the management of assignments, student submissions, and progress tracking in an educational environment. It supports roles for mentors and students, allowing mentors to create assignments, assign them to students, review submissions, and provide feedback.

This system is built using Django and Django REST Framework (DRF), providing a robust and scalable backend for educational platforms.

## Features

- **User Management**: Support for Mentor and Student roles with basic authentication.
- **Assignment Management**: Mentors can create assignments with titles, descriptions, and due dates.
- **Student Assignment Linking**: Assign students to specific assignments.
- **Submission Handling**: Students can submit files for their assigned assignments.
- **Progress Tracking**: Mentors can review submissions and provide feedback with status updates (Completed/Incomplete).
- **RESTful API**: Fully REST-compliant endpoints for all operations.
- **Filtering and Querying**: APIs support query parameters for filtering data (e.g., by mentor or assignment).

## Installation

Follow these steps to set up the project locally:

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment tool (e.g., venv)
- Git (for cloning the repository)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd Student_management_system
   ```

2. **Create and Activate Virtual Environment**:
   ```bash
   python -m venv virtual_env
   # On Windows:
   virtual_env\Scripts\activate
   # On macOS/Linux:
   source virtual_env/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Navigate to the Project Directory**:
   ```bash
   cd project
   ```

5. **Run Database Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a Superuser (Optional, for Admin Access)**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```
   The API will be available at `http://127.0.0.1:8000/`.

## Usage

### API Base URL
All API endpoints are prefixed with `/api/` (assuming you configure it in your main `urls.py`). For example, if your Django project is set up with `/api/` as the base, endpoints will be like `http://127.0.0.1:8000/api/assignments/create/`.

### Authentication
- The system uses basic authentication. Include credentials in requests where required.
- For production, implement token-based authentication (e.g., via DRF's TokenAuthentication).

### API Endpoints

#### Assignments
- **Create Assignment** (Mentors only):
  - **Endpoint**: `POST /assignments/create/`
  - **Description**: Create a new assignment.
  - **Request Body**:
    ```json
    {
      "mentor": 1,
      "title": "Math Assignment",
      "description": "Solve the problems.",
      "due_date": "2025-12-31"
    }
    ```
  - **Response**: Assignment details.

- **Assign Students to Assignment**:
  - **Endpoint**: `POST /assignments/assign/`
  - **Description**: Link students to an assignment.
  - **Request Body**:
    ```json
    {
      "student": 1,
      "assignment": 1
    }
    ```
  - **Response**: StudentAssignment details.

#### Submissions
- **Create Submission** (Students only):
  - **Endpoint**: `POST /submissions/create/`
  - **Description**: Submit a file for an assigned assignment.
  - **Request Body**: Multipart form data with `student_assignment` (ID) and `file`.
  - **Response**: Submission details.

#### Mentor Views
- **List Submissions for Mentor**:
  - **Endpoint**: `GET /mentor/submissions/?mentor_id=<id>`
  - **Description**: Retrieve all submissions for assignments mentored by the specified mentor, including student names, assignment titles, mentor names, and feedback.
  - **Response Example**:
    ```json
    [
      {
        "id": 1,
        "student_name": "John Doe",
        "assignment_title": "Math Assignment",
        "mentor_name": "Dr. Smith",
        "feedback": "Good work!",
        "file": "/media/submissions/file.pdf",
        "submitted_at": "2025-12-25T10:00:00Z"
      }
    ]
    ```

#### Progress
- **Create/Update Progress** (Mentors only):
  - **Endpoint**: `POST /progress/create/`
  - **Description**: Review a submission and add feedback/status.
  - **Request Body**:
    ```json
    {
      "submission": 1,
      "status": "COMPLETED",
      "feedback": "Excellent submission."
    }
    ```
  - **Response**: Progress details.

### Example API Usage with cURL

1. **Create an Assignment**:
   ```bash
   curl -X POST http://127.0.0.1:8000/assignments/create/ \
   -H "Content-Type: application/json" \
   -d '{"mentor": 1, "title": "Science Project", "description": "Build a model.", "due_date": "2025-12-31"}'
   ```

2. **List Submissions for a Mentor**:
   ```bash
   curl -X GET "http://127.0.0.1:8000/mentor/submissions/?mentor_id=1"
   ```

### Testing the API
- Use tools like Postman, Insomnia, or cURL for testing endpoints.
- Access the Django admin at `http://127.0.0.1:8000/admin/` (if superuser created) to manage data.

## Project Structure

```
Student_management_system/
├── requirements.txt          # Python dependencies
├── project/                  # Django project directory
│   ├── manage.py
│   ├── project/              # Main project settings
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── ...
│   ├── accounts/             # App for users (Mentor, Student)
│   │   ├── models.py
│   │   ├── serializers.py
│   │   └── ...
│   ├── assignments/          # App for assignments, submissions, progress
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── ...
│   └── db.sqlite3            # SQLite database
└── virtual_env/              # Virtual environment
```

 

 

 
<parameter name="filePath">c:\Users\pramish\Desktop\Student_management_system\README.md