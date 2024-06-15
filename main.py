from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

user_db = {
    '1': {'FirstName': 'John', 'LastName': 'Doe', 'Email': 'johndoe@gmail.com', 'Country': 'England',
          'Phone': '08899990', 'Languages': ['Python', 'Java', 'C++', 'Ruby', 'Javascript', 'PHP'], 'experience': 2,
          'salary': 25000, 'Certify': True},
    '2': {'FirstName': 'Semen', 'LastName': 'Jack', 'Email': 'seaman@gmail.com', 'Country': 'Romania',
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
        max_id = max(int(uid) for uid in user_db.keys())
        return str(max_id + 1)
    else:
        return '1'


# Create User
@app.post('/form/')
def create_user(user: FormData):
    new_user = user.FirstName
