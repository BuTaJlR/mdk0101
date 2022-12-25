import requests

def login(user_login: str, user_password: str):
    answer = requests.post(
        url='http://127.0.0.1:8000/user/login',
        data=f'{{ "login": "{user_login}", "password": "{user_password}" }}').json()

    return answer

def register(user_login: str, user_password: str):
    answer = requests.post(
        url='http://127.0.0.1:8000/user/register',
        data=f'{{ "login": "{user_login}", "password": "{user_password}" }}').json()
    return answer

def get(id:int):
    answer = requests.get(
        url=f'http://127.0.0.1:8000/user/get/{id}',
    )
    return answer.json()

def getAll(table:str):
    answer = requests.get(
        url=f'http://127.0.0.1:8000/{table}/',
    )
    return answer.json()
