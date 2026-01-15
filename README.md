# Employee Management System (Flask API)

A simple **Employee Management System REST API** built using **Flask**, **Flask-SQLAlchemy**, **Flask-JWT-Extended**, and **Marshmallow**. This project demonstrates CRUD operations, authentication using JWT, pagination, and filtering.

---

## 🚀 Features

* JWT-based authentication (Login)
* Create, Read, Update, Delete (CRUD) Employees
* Pagination support
* Filter employees by department and role
* MySQL database integration using SQLAlchemy
* Input validation using Marshmallow schemas

---

## 🛠 Tech Stack

* Python 3.x
* Flask 3.x
* Flask-SQLAlchemy
* Flask-JWT-Extended
* Marshmallow
* MySQL
* Postman (for API testing)

---

## 📁 Project Structure

```
Employee_Management_System/
│
├── app.py              # Application entry point
├── config.py           # Configuration settings
├── extensions.py       # Database instance
├── models.py           # Database models
├── schemas.py          # Marshmallow schemas
├── routes.py           # Employee APIs
├── auth.py             # Authentication APIs
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── venv/               # Virtual environment
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone <repository-url>
cd Employee_Management_System
```

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Database

Edit **config.py**:

```python
class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:password@localhost/employee"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "your-secret-key"
    JWT_ACCESS_TOKEN_EXPIRES = 86400  # 24 hours
```

Create MySQL database:

```sql
CREATE DATABASE employee;
```

---

## ▶️ Run the Application

```bash
python app.py
```

Server will start at:

```
http://127.0.0.1:5000
```

---

## 🔐 Authentication

### Login

**POST** `/api/login`

```json
{
  "username": "admin",
  "password": "admin"
}
```

Response:

```json
{
  "access_token": "<JWT_TOKEN>"
}
```

Use this token in headers:

```
Authorization: Bearer <JWT_TOKEN>
```

---

## 📌 API Endpoints

### ➕ Create Employee

**POST** `/api/employees/`

```json
{
  "name": "John",
  "email": "john@example.com",
  "department": "HR",
  "role": "Manager"
}
```

---

### 📄 List Employees

**GET** `/api/employees/?page=1&department=HR&role=Manager`

Response:

```json
{
  "total": 10,
  "page": 1,
  "employees": []
}
```

---

### 🔍 Get Employee by ID

**GET** `/api/employees/{id}/`

* Returns **404** if employee not found

---

### ✏️ Update Employee

**PUT** `/api/employees/{id}/`

```json
{
  "role": "Senior Developer"
}
```

---

### ❌ Delete Employee

**DELETE** `/api/employees/{id}/`

* Returns **204 No Content**

---

## 🧪 Testing with Postman

1. Login and copy JWT token
2. Add token to Authorization header
3. Call secured APIs

---

## ⚠️ Common Errors & Fixes

* **Token expired** → Login again to get a new token
* **404 Not Found** → Check URL and employee ID
* **Unknown field error** → Ensure JSON matches schema fields

---

## 📌 Future Enhancements

* User roles (Admin/User)
* Refresh tokens
* Swagger / OpenAPI documentation
* Docker support
* Unit testing with PyTest

---

## 👨‍💻 Author

**Employee Management System**

Built for learning Flask REST APIs, authentication, and backend fundamentals.

---

⭐ If you like this project, feel free to extend it or use it for learning!
