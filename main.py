from fastapi import FastAPI
from models import *

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("590af753-4882-452a-9932-1ba3a4aabb39"),
        first_name="Kilian",
        last_name="Luu",
        middle_name="Sky",
        gender=Gender.male,
        roles=[Role.student]
    ),
    User(
        id=UUID("74b8fc17-1032-4f7a-bef7-daaef9e3d4d3"),
        first_name="Alex",
        last_name="Smith",
        middle_name="Blue",
        gender=Gender.male,
        roles=[Role.student]
    )
]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/v1/users")
async def fetch_users():
    return db


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user in db:
            if user.id == user_id:
                db.remove(user)
                return
