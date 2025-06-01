from fastapi import FastAPI
from typing import Optional

api = FastAPI()

@api.get('/')
def get_index(argument1):
    return {
        'data': argument1
    }
#curl -X GET -i http://127.0.0.1:8000/?argument1=hello%20world
#curl -X GET -i http://127.0.0.1:8000/
#  "GET / HTTP/1.1" 422 Unprocessable Entity

@api.get('/typed')
def get_typed(argument1: int):
    return {
        'data': argument1 + 1
    }

#curl -X GET -i http://127.0.0.1:8000/typed?argument1=1234

#curl -X GET -i http://127.0.0.1:8000/typed?argument1=hello


@api.get('/addition')
def get_addition(a: int, b: Optional[int]=None):
    if b:
        result = a + b
    else:
        result = a + 1
    return {
        'addition_result': result
    }

# mettre les URL avec -> & <- entre guillemets dans curl
#curl -X GET -i 'http://127.0.0.1:8000/addition?a=1&b=5'

