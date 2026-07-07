# NotesApp API

A beginner-friendly RESTful Notes API built with FastAPI to learn backend development fundamentals. The project demonstrates authentication with JWT, CRUD operations, PostgreSQL integration using SQLAlchemy, Docker containerization, and cloud deployment with Railway.



## Features

- User registration
- JWT authentication
- Password hashing with bcrypt
- Create, Read, Update and Delete notes
- Protected API endpoints
- PostgreSQL database
- Dockerized application
- Railway deployment


## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker
- Railway
- JWT Authentication


## Running Locally

### Clone the repository

```bash
git clone https://github.com/hooryasinwani/notesapp
cd notesapp
```

### Create a `.env` file

```env
SECRET_KEY=your_secret_key
ALGORITHM=HS256
DATABASE_URL=your_database_url
```

### Run with Docker

```bash
docker compose up --build
```

Swagger UI:

```
http://localhost:8000/docs
```

---

## Live Demo

Swagger Documentation:


https://notesapp-production-3441.up.railway.app/docs


---

## API Documentation

![Swagger UI](images/swagger-ui.png)

## Future Improvements

- Alembic migrations
- Automated testing
- Refresh tokens
- User roles and permissions
- Pagination
- API rate limiting

---

## What I Learned

This project was built to learn core backend development concepts including:

- REST API development with FastAPI
- SQLAlchemy ORM
- PostgreSQL
- JWT authentication
- Password hashing
- Docker and Docker Compose
- Cloud deployment with Railway
