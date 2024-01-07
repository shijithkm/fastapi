# from typing import Union

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

from uuid import uuid4
from models import Gender, Role, User
from fastapi import FastAPI
from typing import List, Union


app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        first_name="Shijith",
        middle_name="Kandirithy",
        last_name="Mohanan",
        gender=Gender.male,
        roles=[Role.admin,Role.user]
        ),
         User(
        id=uuid4(),
        first_name="Sinju",
        middle_name="Kandirithy",
        last_name="Shijith",
        gender=Gender.female,
        roles=[Role.user]
        ),
        User(
        id=uuid4(),
        first_name="Tara",
        middle_name="Kandirithy",
        last_name="Shijith",
        gender=Gender.female,
        roles=[Role.student]
        ),
        User(
        id=uuid4(),
        first_name="Jeeva",
        middle_name="Kandirithy",
        last_name="Shijith",
        gender=Gender.male,
        roles=[Role.student]
        )
]

@app.get("/")
def root():
    return {"hello":"fastapi"}

@app.get("/items/{item_id}")
def read_item(item_id: int,q: Union[str,None] = None):
    return {"item_id":item_id,"q":q}

@app.get("/api/v1/users")
async def users():
    return db