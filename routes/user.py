from fastapi import APIRouter
from config.db import client as db
from schemas.user import userEntity, usersEntity
from models.user import User

user = APIRouter()

@user.get('/users')
def find_all_users():
    return usersEntity(db.user.find())

@user.get('/users/{id}')
def find_user():
    return {'Hello': 'World'}

@user.post('/users')
def create_user(user: User):
    new_user = dict(user)
    id = db.user.users.insert_one(new_user).inserted_id
    return {'user_id': str(id)}

@user.put('/users/{id}')
def update_user():
    return {'Hello': 'World'}

@user.delete('/users/{id}')
def delete_user():
    return {'Hello': 'World'}