
from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

# Now get them like this:
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

print(DB_HOST, DB_USER)  # Just to test!


from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import mysql.connector
from passlib.context import CryptContext

# ✅ Create FastAPI app
app = FastAPI()

# ✅ CORS settings
origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "http://localhost",
    "http://127.0.0.1",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ✅ Pydantic model
class User(BaseModel):
    email: str
    username: str | None = None
    password: str

# ✅ DB connection
def get_db():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,   # <- change this!
        database=DB_NAME            # <- change this if needed
    )

# ✅ Signup route
@app.post("/signup")
async def signup(user: User):
    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)

        # ✅ Check if email exists
        cursor.execute("SELECT id FROM users WHERE email = %s", (user.email,))
        if cursor.fetchone():
            raise HTTPException(status_code=400, detail="Email already exists")

        # ✅ Check if username exists
        cursor.execute("SELECT id FROM users WHERE username = %s", (user.username,))
        if cursor.fetchone():
            raise HTTPException(status_code=400, detail="Username already exists")

        # ✅ Hash password
        hashed_password = pwd_context.hash(user.password)

        # ✅ Insert new user
        cursor.execute(
            "INSERT INTO users (email, username, password) VALUES (%s, %s, %s)",
            (user.email, user.username, hashed_password)
        )
        db.commit()
        cursor.close()
        db.close()

        return {"status": "success", "message": "User registered successfully!"}

    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=str(e))

# ✅ Login route
@app.post("/login")
async def login(user: User):
    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM users WHERE email = %s",
            (user.email,)
        )
        result = cursor.fetchone()
        print("DB result:", result)

        if result:
            stored_hash = result["password"]
            if pwd_context.verify(user.password, stored_hash):
                return {"status": "success", "message": "Login successful!"}
            else:
                raise HTTPException(status_code=401, detail="Invalid email or password")
        else:
            raise HTTPException(status_code=401, detail="Invalid email or password")

    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=str(e))

# ✅ Test route
@app.get("/")
def root():
    return {"status": "success", "message": "FastAPI working!"}
