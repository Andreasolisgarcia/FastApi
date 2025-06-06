from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    user_id: int
    name: str
    subscription: Optional[str]= None 

users_db = [
    {
        'user_id': 1,
        'name': 'Alice',
        'subscription': 'free tier'
    },
    {
        'user_id': 2,
        'name': 'Bob',
        'subscription': 'premium tier'
    },
    {
        'user_id': 3,
        'name': 'Clementine',
        'subscription': 'free tier'
    }
]

api = FastAPI()
# GET / renvoie un message de bienvenue
@api.get('/')
def get_index():
    return {
        'greetings': 'welcome'
    }
# GET /users renvoie la base de donnée en entier

@api.get('/users')
def get_users():
    return users_db

# GET /users/userid renvoie toutes les données d'un utilisateur en fonction de son id. userid devra être un nombre entier. Si le userid fourni ne correspond pas à un utilisateur existant, on retournera un dictionnaire vide.
@api.get('/users/{userid:int}')
def get_user(userid):
    try:
        user = list(filter(lambda x: x.get('user_id') == userid, users_db))[0]
        return user
    except IndexError:
        return {}
    
# GET /users/userid/name renvoie le nom d'un utilisateur en fonction de son id. userid devra être un nombre entier. Si le userid fourni ne correspond pas à un utilisateur existant, on retournera un dictionnaire vide.
@api.get('/users/{userid:int}/name')
def get_user_name(userid):
    try:
        user = list(filter(lambda x: x.get('user_id') == userid, users_db))[0]
        return {'name': user['name']}
    except IndexError:
        return {}

# GET /users/userid/subscription renvoie le type d'abonnement d'un utilisateur en fonction de son id. userid devra être un nombre entier
@api.get('/users/{userid:int}/subscription')
def get_user_suscription(userid):
    try:
        user = list(filter(lambda x: x.get('user_id') == userid, users_db))[0]
        return {'subscription': user['subscription']}
    except IndexError:
        return {}
    
# PUT /users crée un nouvel utilisateur dans la base de données et renvoie les données de l'utilisateur créé. Les données sur le nouvel utilisateur doivent être fournies dans le corps de la requête.
@api.put('/users')
def post_user(user: User):
    return user


# POST /users/userid modifie les données relatives à l'utilisateur identifié par userid et renvoie les données de l'utilisateur modifié. Les données sur l'utilisateur à modifier doivent être fournies dans le corps de la requête

# DELETE /users/userid supprime l'utilisateur désigné par userid et renvoie une confirmation de la suppression.