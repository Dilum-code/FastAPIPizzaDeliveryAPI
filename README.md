FastAPI Pizza Delivery API

A simple Pizza Delivery API built with FastAPI. This project demonstrates how to build, test, and secure a RESTful API with JWT authentication, database integration (SQLite), and Docker support.



Features

- User registration and login (JWT-based authentication)
- Add, list, and fetch pizzas
- Place and view pizza orders
- SQLite database via SQLAlchemy
- Token-protected routes (`/me`, `/order`, `/orders`)
- Dockerized for easy deployment



Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [SQLite](https://www.sqlite.org/)
- [JWT](https://jwt.io/)
- [Docker](https://www.docker.com/)
- [Postman](https://www.postman.com/) (for testing)



Getting Started

Clone the Repository

```bash
git clone https://github.com/yourusername/fastapi-pizza-api.git
cd fastapi-pizza-api

Create Virtual Environment & Install Dependencies

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt

Run the API

uvicorn main:app --reload

