from fastapi import FastAPI
from models.models import User, Feedback

user = User(id=1,  name="John Doe")

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# новый роут
@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!"}


# новый роут
@app.get("/users")
def read_custom_message():
    return user


bd = []

@app.post("/feedback")
async def post_feedback(feedback: Feedback):
    bd.append({"name": feedback.name, "message": feedback.message})
    return f"Feedback received. Thank you, {feedback.name}!"

@app.get("/comments")
async def show_messages():
    return bd

@app.delete("/delete")
async def show_messages():
    del bd[0]
    return bd

