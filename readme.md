

# VaultAuth

## 📌 Project Overview

**VaultAuth** is a simple yet secure **user authentication system** built with **FastAPI**.  
It provides basic **Sign Up** and **Login** functionality, connects to a database to store user credentials, and uses environment variables to safely manage sensitive information.


## ✨ Key Features

- ✅ **User Registration:** New users can create an account with email and password.
- ✅ **User Login:** Existing users can log in with their credentials.
- ✅ **Database Integration:** User data is securely stored in a database (e.g., MySQL, PostgreSQL, or SQLite).
- ✅ **Environment Variables:** Uses a `.env` file to keep database credentials and other secrets out of the source code.
- ✅ **.gitignore:** Ensures that your secrets and temporary files never get pushed to GitHub.

---

## 📂 Project Structure

```

VaultAuth/
├── main.py
├── signin.html
├── login.html
├── DATABASE.sql
├── .env
├── .gitignore
└── README.md

````

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Shannaseem/AccessPoint-.git
cd AccessPoint


---

### 2️⃣ Create and Activate a Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install fastapi uvicorn python-dotenv
```

---

## 🔑 Using Environment Variables

1. In your project root, create a file named `.env`.

2. Add your database configuration. Replace placeholder values with your actual details:

   ```env
   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=your_db_password
   DB_NAME=your_db_name
   ```

3. **Never push `.env` to GitHub!**
   Make sure your `.gitignore` includes:

   ```
   .env
   __pycache__/
   *.pyc
   tempCodeRunnerFile.py
   ```

4. In your `main.py`, load the environment variables:

   ```python
   from dotenv import load_dotenv
   import os

   load_dotenv()

   DB_HOST = os.getenv("DB_HOST")
   DB_USER = os.getenv("DB_USER")
   DB_PASSWORD = os.getenv("DB_PASSWORD")
   DB_NAME = os.getenv("DB_NAME")
   ```

---

## 🚀 Running the Project

Run the FastAPI app locally with **Uvicorn**:

```bash
uvicorn main:app --reload
```

* Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to test your API routes.
* Use your `signin.html` and `login.html` pages for user interaction.


## 🔒 Best Practices

✅ Use `.env` to manage secrets securely.
✅ Always include `.env` in `.gitignore`.
✅ Never commit your database credentials.
✅ Rotate your secrets if they ever leak.
✅ Test your `.gitignore` by running `git status` before committing.


## 🙌 Author

**Project:** VaultAuth
**Author:** *Shannaseem*
**Tech Stack:** Python, FastAPI, Uvicorn, HTML, dotenv

---

## ✅ License

This project is open for learning and personal use.
**Keep your credentials safe!**
