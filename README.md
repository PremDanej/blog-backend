# Blog-Backend

This is Blog-Backend application for just learning purpose. Using **SQLite** with **SQLAlchemy** and **FastAPI**.

### Project Structure

```text
blog-backend/
├── app/
│   ├── auth/
│   ├── blog/
│   ├── connection/
│   ├── hashing/
│   └── model/
│       ├── request/
│       └── response/
│   ├── repository/
│   ├── routers/
│   ├── schema/
│   └── requirements.txt
├── requirements.txt
├── run.py
├── Dockerfile.txt
├── docker-compose.yml
└── .env
```

### Tools

- Python language
- Fast API
- Uvicorn Server
- SQLAlchemy
- JWT

### What cover?

- Easily understandable folder structure
- Relational database
- Database connection
- Table schemas
- HTTP methods + Status code
- CRUD APIs
- Routing + Dynamic routing
- Request Body
- Request - Response models
- Handling errors
- OAuth2 with Password + Bearer JWT token
- Hashing for encryption
- Advance - OAuth2 scopes
- Scopes wise API's permission

### Getting started

1. Clone this repository
   ``` commandline
   git clone https://github.com/PremDanej/blog-backend.git
   ```

2. Go to the main folder
   ``` commandline
   cd blog-backend
   ```

3. Create virtual environment
   ``` commandline
   python -m venv .venv
   ```

4. Create `.env` file and paste it
   ``` properties
   HOST=127.0.0.1
   PORT=8000
   ```

5. Install all dependencies -
   ``` requirements
   pip install -r requirements.txt
   ```

6. Run the project by
   ``` commandline
   python run.py 
   ----- OR -----
   uvicorn app.blog.main:app --reload
   ```