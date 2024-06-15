from http.client import HTTPException
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

user_db = {
    1: {'id': 1, 'FirstName': 'John', 'LastName': 'Doe', 'Email': 'johndoe@gmail.com', 'Country': 'England',
        'Phone': '08899990', 'Languages': ['Python', 'Java', 'C++', 'Ruby', 'Javascript', 'PHP'], 'experience': 2,
        'salary': 25000, 'Certify': True},
    2: {'id': 2, 'FirstName': 'Semen', 'LastName': 'Jack', 'Email': 'seaman@gmail.com', 'Country': 'Romania',
        'Phone': '9888788', 'Languages': ['Python', 'Java', 'C++'], 'experience': 2, 'salary': 13000, 'Certify': True}
}


class FormData(BaseModel):
    FirstName: str
    LastName: str
    Email: str
    Country: str
    Phone: str
    Languages: List[str]
    experience: int
    salary: float
    Certify: bool


# Function to generate unique id
def generate_new_id():
    if user_db:
        max_id = max(user_db.keys())
        return max_id + 1
    else:
        return 1


# Create User
@app.post('/user/')
def create_user(user: FormData):
    new_id = generate_new_id()
    user_dict = user.dict()
    user_dict['id'] = new_id
    user_db[new_id] = user_dict
    return user_dict


# Get All the users
@app.get("/")
def get_users():
    user_list = list(user_db.values())
    return user_list


# Get All the users
@app.get("/users")
def get_users():
    user_list = list(user_db.values())
    return user_list


# Get a user by id
@app.get("/users/{id}")
def get_user_byid(id: int):
    if id in user_db:
        return user_db[id]
    else:
        raise HTTPException()


# Delete User
@app.delete("/users/{id}")
def delete_user(id: int):
    if id in user_db:
        del user_db[id]
        return "Successfully deleted user with id {}".format(id)


# Update User
@app.put("/users/{id}")
def update_user(id: int, user_data: FormData):
    if id in user_db:
        user_db[id].update(user_data.dict())
        user_db[id]['id'] = id
        return user_db[id]

    else:
        raise HTTPException("User Not found")

