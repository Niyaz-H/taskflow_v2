# TaskFlow v2 - Enhanced Task Management Application

TaskFlow is a full-stack task management application built with Django and Django Rest Framework. It features both a RESTful API and a clean web interface for managing tasks with user authentication. This version includes enhanced features like task priorities, due dates, filtering, and pagination.

## Features

### Web Interface
*   **User Registration & Login:** Simple and intuitive user registration and login forms
*   **Task Management:** Create, view, update, complete, and delete tasks through a clean web interface
*   **Task Priorities & Due Dates:** Set priorities (Low, Medium, High) and due dates for your tasks.
*   **Filtering:** Filter tasks by completion status and priority.
*   **Pagination:** Paginated task list for better performance with a large number of tasks.
*   **Real-time Updates:** Dynamic task list that updates without page refreshes
*   **Responsive Design:** Clean, modern interface that works on all devices

### API Endpoints
*   `GET /`: Web interface for task management
*   `GET /api/`: API root with available endpoints
*   `POST /api/register/`: Register a new user
*   `POST /api/api-token-auth/`: Log in and receive an authentication token
*   `GET /api/tasks/`: List all of your tasks.
    *   Filter by completion status: `?completed=true` or `?completed=false`
    *   Filter by priority: `?priority=H`, `?priority=M`, or `?priority=L`
*   `POST /api/tasks/`: Create a new task.
*   `GET /api/tasks/<id>/`: Retrieve a specific task.
*   `PUT /api/tasks/<id>/`: Update a specific task.
*   `DELETE /api/tasks/<id>/`: Delete a specific task.

## Technology Stack

*   **Backend:** Python, Django, Django Rest Framework
*   **Frontend:** HTML, CSS, JavaScript (Vanilla)
*   **Database:** PostgreSQL
*   **Authentication:** Token-based authentication with Django's built-in auth system
*   **API:** RESTful API with CORS support
*   **Deployment:** Docker & Docker Compose

## Getting Started

### Prerequisites

*   Docker
*   Docker Compose

### Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/Niyaz-H/taskflow_v2.git
    ```

2.  Navigate to the project directory:

    ```bash
    cd taskflow_v2
    ```

3.  Build and run the Docker containers:

    ```bash
    docker-compose up --build -d
    ```

4.  Apply the database migrations:

    ```bash
    docker-compose exec web python manage.py migrate
    ```

5.  Create a superuser (optional, for admin access):

    ```bash
    docker-compose exec web python manage.py create_superuser
    ```

### Using the Application

#### Web Interface

1. Open your browser and navigate to `http://localhost:8000`
2. Register a new account or log in with existing credentials
3. Start managing your tasks through the clean web interface

#### API Usage

The API will be available at `http://localhost:8000/api/`. You can use tools like [Postman](https://www.postman.com/) or `curl` to interact with the API.

**1. Register a new user:**

```bash
curl -X POST http://localhost:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "yourusername", "password": "yourpassword"}'
```

**2. Log in and get a token:**

```bash
curl -X POST http://localhost:8000/api/api-token-auth/ \
  -H "Content-Type: application/json" \
  -d '{"username": "yourusername", "password": "yourpassword"}'
```

**3. Create a new task:**

```bash
curl -X POST http://localhost:8000/api/tasks/ \
  -H "Authorization: Token YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title": "My first task", "description": "This is a description of my first task.", "priority": "H", "due_date": "2025-12-31T23:59:59Z"}'
```

**4. List all tasks:**

```bash
curl -X GET http://localhost:8000/api/tasks/ \
  -H "Authorization: Token YOUR_TOKEN"
```

## Key Features Demonstrated

### Backend Development
- Django project structure and configuration
- RESTful API design with Django Rest Framework
- Database modeling with Django ORM
- User authentication and authorization
- Token-based API authentication
- CORS configuration for API access
- API filtering and pagination

### Database Management
- PostgreSQL integration
- Database migrations
- Model relationships (User -> Tasks)
- Query optimization

### DevOps & Deployment
- Docker containerization
- Docker Compose for multi-service setup
- Environment configuration
- Production-ready setup

### Frontend Integration
- API consumption with JavaScript
- Dynamic DOM manipulation
- Token-based authentication flow
- Responsive web design

## Project Structure

```
taskflow_v2/
├── Dockerfile                 # Docker configuration
├── docker-compose.yml        # Multi-service Docker setup
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── README.md                # Project documentation
├── taskflow/                # Main project directory
│   ├── settings.py          # Django settings
│   ├── urls.py              # URL routing
│   └── wsgi.py              # WSGI application
└── tasks/                   # Tasks application
    ├── models.py            # Data models
    ├── serializers.py       # API serializers
    ├── views.py             # API views and web views
    ├── urls.py              # App URL routing
    ├── templates/           # HTML templates
    └── migrations/          # Database migrations
```

This project demonstrates proficiency in full-stack web development, API design, database management, and modern deployment practices using Docker.