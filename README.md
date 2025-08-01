
# 🧩 Project Name: AUTHAPI

## 📌 About the Project

**AUTHAPI** is a Django REST API for user authentication. It supports registration, login, and profile management using JSON Web Tokens (JWT) for secure access.

---

## 🚀 Getting Started

### ✅ 1. Clone the Repository

```bash
git clone https://github.com/yourusername/AUTHAPI.git
cd authapi
```

---

### ✅ 2. Create and Activate a Virtual Environment

#### For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### For macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### ✅ 3. Install Dependencies from `requirements.txt`

```bash
pip install -r requirements.txt
```

---

### ✅ 4. Set Up Environment Variables

Create a `.env` file in the project root with:

```env
SECRET_KEY=your-django-secret-key
DEBUG=True
```

---

### ✅ 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### ✅ 6. Run the Development Server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔐 Authentication Endpoints

All routes are under the **users** app.

| Method | Endpoint     | Description               | Auth Required | Status     |
|--------|--------------|---------------------------|---------------|------------|
| POST   | `/register/` | Register a new user       | ❌            | ✅ Working |
| POST   | `/login/`    | Login and get JWT tokens  | ❌            | ✅ Working |
| GET    | `/me/`       | Get current user profile  | ✅ (Bearer)    | ✅ Working |

---

## 🧪 Endpoint Testing Examples

### 🟢 Register a User

**POST** `/register/`

```json
{
  "username": "crown",
  "email": "crown@mj.com",
  "password": "secure123",
  "profile": {
    "phone_number": "09011223344",
    "role": "student",
    "date_of_birth": "2001-10-10"
  }
}
```

### ✅ Response:

```json
{
  "user": {
    "id": 1,
    "username": "crown",
    "email": "crown@mj.com",
    "profile": {
      "phone_number": "09011223344",
      "role": "student",
      "date_of_birth": "2001-10-10"
    }
  },
  "refresh": "your-refresh-token",
  "access": "your-access-token"
}
```

---

### 🔑 Login

**POST** `/login/`

```json
{
  "email": "crown@mj.com",
  "password": "secure123"
}
```

**Response:**
```json
{
  "refresh": "your-refresh-token",
  "access": "your-access-token"
}
```

---

### 👤 Get Authenticated User

**GET** `/me/`  
**Headers:**
```http
Authorization: Bearer your-access-token
```

**Response:**
```json
{
  "id": 1,
  "username": "crown",
  "email": "crown@mj.com",
  "profile": {
    "phone_number": "09011223344",
    "role": "student",
    "date_of_birth": "2001-10-10"
  }
}
```

---

## 🧪 Run Tests

```bash
python manage.py test
```

---

## 🛠 Tech Stack

- Python 3.10+
- Django ≥ 4.x
- Django REST Framework
- SimpleJWT
- python-dotenv

---

## 📁 Project Structure

```
AUTHAPI/
│
├── authapi/          # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── users/            # Authentication app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── .env              # Environment secrets
├── .gitignore
├── db.sqlite3
├── manage.py
├── requirements.txt
└── venv/
```

---

## ✍️ Author

- **Matthew Ohimai**
- GitHub: [@yourusername](https://github.com/MatthewOhimai)
- X (Twitter): [@MatthewOhimai](https://x.com/MatthewOhimai)

---


