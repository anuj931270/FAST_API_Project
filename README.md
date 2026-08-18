# FAST API Project – Anuj Tour & Travels

## 📌 Project Overview

**Anuj Tour & Travels** is a full-stack travel management web application developed using a frontend application, FastAPI backend, and MongoDB database.

The main purpose of this project is to provide a simple platform where users can interact with a travel website, register/login, and manage travel-related information through a backend API.

The project follows a **frontend → backend API → database** architecture.

### Technology Flow

```text
User
  ↓
Frontend – Anuj Tour & Travels
  ↓
FastAPI Backend
  ↓
MongoDB Database
```

---

# 🚀 Project Features

* Responsive travel website frontend
* User registration and login
* Backend REST APIs using FastAPI
* MongoDB database integration
* User data management
* Travel/destination data management
* API-based communication between frontend and backend
* Authentication and security utilities
* Structured project using routes, schemas, models, and utility modules
* API documentation using FastAPI Swagger UI

---

# 🎨 Frontend

The frontend of the project was developed as the **Anuj Tour & Travels** application.

The frontend provides the user interface through which users can interact with the travel application.

### Frontend Responsibilities

* Display travel-related information
* Provide registration and login pages
* Provide customer dashboard
* Provide admin dashboard
* Display customer information
* Provide destination/travel-related pages
* Send requests to the backend
* Display backend responses to users

### Frontend Technologies

* HTML
* CSS
* Flask/Jinja Templates

The frontend contains reusable templates such as:

```text
templates/
├── base.html
├── home.html
├── login.html
├── register.html
├── customer_dashboard.html
├── admin_dashboard.html
└── customer_list.html
```

The `base.html` template can be used as a common layout for other pages, which helps maintain a consistent UI across the application.

---

# ⚙️ Backend – FastAPI

For the backend, I used **FastAPI**, a modern Python framework for building high-performance REST APIs.

FastAPI is responsible for handling requests coming from the frontend and communicating with the MongoDB database.

### Backend Responsibilities

* Handle HTTP requests
* Create REST APIs
* Process user registration
* Handle user-related operations
* Validate incoming data
* Communicate with MongoDB
* Return JSON responses
* Handle authentication/security-related functionality

### Backend Structure

```text
FastAPI_MongoDB/
│
├── routes/
│   └── get_users.py
│
├── schemas/
│   ├── user.py
│   └── destinations.py
│
├── utils/
│   └── security.py
│
└── main.py
```

---

# 🔌 API Architecture

The backend follows a REST API architecture.

The frontend sends HTTP requests to FastAPI endpoints.

For example:

```text
Frontend
   ↓
HTTP Request
   ↓
FastAPI Endpoint
   ↓
Validation
   ↓
MongoDB
   ↓
FastAPI Response
   ↓
Frontend
```

This separation makes the application easier to maintain and allows the frontend and backend to work independently.

---

# 🗄️ Database – MongoDB

I used **MongoDB** as the database for storing application data.

MongoDB is a NoSQL database that stores data in a document-oriented format.

### Why MongoDB?

* Easy to work with JSON-like documents
* Flexible schema
* Suitable for API-based applications
* Easy integration with Python
* Good choice for applications where data structures may change

The FastAPI backend communicates with MongoDB to store and retrieve application data.

### Basic Data Flow

```text
User Registration
       ↓
Frontend
       ↓
FastAPI API
       ↓
Data Validation
       ↓
MongoDB
       ↓
User Data Stored
```

---

# 🔐 Authentication and Security

The project also contains security-related utilities in the backend.

The authentication flow is designed to handle user-related access securely.

Basic flow:

```text
User
 ↓
Login/Register
 ↓
FastAPI
 ↓
Validate User Data
 ↓
Check/Store Data in MongoDB
 ↓
Return Response
```

Sensitive configuration such as database credentials should be stored in environment variables rather than directly inside the source code.

Example:

```text
.env
```

The `.env` file should not be committed to GitHub.

---

# 📋 Pydantic Schemas

The FastAPI backend uses schemas to define and validate the structure of request and response data.

For example:

```text
schemas/
├── user.py
└── destinations.py
```

Schemas help ensure that the API receives data in the expected format.

Example concept:

```text
Client Request
      ↓
Pydantic Schema
      ↓
Validate Data
      ↓
FastAPI
      ↓
MongoDB
```

This helps reduce invalid data and makes the API more reliable.

---

# 🛣️ API Routes

The backend separates API functionality into different route modules.

For example:

```text
routes/
└── get_users.py
```

Keeping routes in separate files makes the project more organized and easier to maintain.

Instead of keeping all API endpoints inside one large file, different functionalities can be separated into individual route modules.

---

# 📚 API Documentation

One of the advantages of FastAPI is automatic API documentation.

After starting the FastAPI server, the interactive Swagger documentation can be accessed through:

```text
/docs
```

For example:

```text
http://127.0.0.1:8000/docs
```

The Swagger UI allows developers to:

* View available APIs
* Understand request parameters
* Test API endpoints
* View request and response formats
* Debug APIs during development

FastAPI can also provide ReDoc documentation through:

```text
/redoc
```

---

# 🧩 Additional FastAPI Application

The project also contains a `Firstapp` application that demonstrates another FastAPI implementation.

Its structure includes:

```text
Firstapp/
├── main.py
├── database.py
├── models.py
├── schema.py
├── requirements.txt
└── staff.json
```

### Purpose of the Components

**main.py**

Contains the main FastAPI application and API endpoints.

**database.py**

Contains database-related configuration and operations.

**models.py**

Defines the structure of application/database models.

**schema.py**

Defines data validation schemas.

**staff.json**

Contains sample staff-related data for the application.

**requirements.txt**

Contains the Python dependencies required to run the application.

---

# 📁 Complete Project Structure

```text
FAST_API_Project/
│
├── anuj-tour-travels/
│   ├── app.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── customer_dashboard.html
│   │   ├── admin_dashboard.html
│   │   └── customer_list.html
│   └── ...
│
├── FastAPI_MongoDB/
│   ├── routes/
│   │   └── get_users.py
│   ├── schemas/
│   │   ├── user.py
│   │   └── destinations.py
│   ├── utils/
│   │   └── security.py
│   └── main.py
│
├── Firstapp/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schema.py
│   ├── requirements.txt
│   └── staff.json
│
├── clean.py
├── README.md
└── .gitignore
```

---

# 🔄 Overall Application Workflow

The complete application works approximately like this:

```text
              USER
                │
                ▼
       Anuj Tour & Travels
           Frontend
                │
                │ HTTP Request
                ▼
          FastAPI Backend
                │
        ┌───────┴────────┐
        │                │
        ▼                ▼
   Pydantic          Security/
    Schemas          Authentication
        │                │
        └───────┬────────┘
                ▼
             MongoDB
                │
                ▼
          Stored Data
                │
                ▼
        FastAPI Response
                │
                ▼
             Frontend
```

---

# 🛠️ Technologies Used

| Technology | Purpose                        |
| ---------- | ------------------------------ |
| Python     | Backend programming            |
| HTML       | Frontend structure             |
| CSS        | Frontend styling               |
| JavaScript | Frontend interaction           |
| Flask      | Frontend/web application layer |
| FastAPI    | REST API backend               |
| MongoDB    | Database                       |
| Pydantic   | Data validation                |
| Uvicorn    | FastAPI server                 |
| Git        | Version control                |
| GitHub     | Source code hosting            |

---

# ▶️ How to Run the Project

## 1. Clone the Repository

```bash
git clone https://github.com/anuj931270/FAST_API_Project.git
```

## 2. Go to the Project Directory

```bash
cd FAST_API_Project
```

## 3. Create a Virtual Environment

```bash
python -m venv myenv
```

## 4. Activate the Environment

### Windows

```powershell
myenv\Scripts\activate
```

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

If separate applications have their own requirements files, install the dependencies required by that application.

## 6. Configure Environment Variables

Create a `.env` file for sensitive configuration such as database connection details.

Example:

```text
MONGO_URI=your_mongodb_connection_string
```

Do not upload the `.env` file to GitHub.

## 7. Start FastAPI

```bash
uvicorn main:app --reload
```

The API will normally be available at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 🎯 Project Objective

The main objective of this project is to understand and implement a complete web application architecture using:

**Frontend + REST API + Database**

Through this project, I worked with:

* Frontend development
* Flask
* FastAPI
* REST APIs
* API routing
* Request/response handling
* Data validation
* MongoDB integration
* Authentication and security concepts
* Project structuring
* Environment variables
* Git and GitHub

---

# 📌 Key Learning

This project helped me understand how different components of a full-stack application communicate with each other.

The most important concept was separating the application into three layers:

```text
Frontend
   ↓
Backend API
   ↓
Database
```

This architecture makes the application more modular, scalable, maintainable, and easier to debug.

---

# 👨‍💻 Author

**Anuj Kumar**

AI Engineer | Python | FastAPI | Machine Learning | Data Science

---

# ⭐ Future Improvements

Possible future improvements include:

* JWT-based authentication
* Role-based access control
* Better API error handling
* Travel booking functionality
* Payment gateway integration
* Image upload for destinations
* Advanced admin dashboard
* Search and filtering
* API testing using Pytest
* Docker deployment
* Cloud deployment
* Better frontend-backend integration
