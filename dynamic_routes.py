from fastapi import FastAPI

api = FastAPI(
    title='My API'
)

@api.get('/')
def get_index():
    return {'data': 'hello world'}

# endpoint dynamique /item
# @api.get('/item/{itemid}')
# def get_item():
#     return {'route': 'dynamic'}

# curl -X GET -i http://127.0.0.1:8000/item/1

# @api.get('/item/{itemid}')
# def get_item(itemid):
#     return {
#         'route': 'dynamic',
#         'itemid': itemid
#         }

#accepte tous les arguments
#ex: curl -X GET -i http://127.0.0.1:8000/item/my_item

# @api.get('/item/{itemid}/description/{language}')
# def get_item_language(itemid, language):
#     if language == 'fr':
#         return {
#             'itemid': itemid,
#             'description': 'un objet',
#             'language': 'fr'
#         }
#     else:
#         return {
#             'itemid': itemid,
#             'description': 'an object',
#             'language': 'en'
#         }

#Type controle 

# @api.get('/item/{itemid:int}')
# def get_item(itemid):
#     return {
#         'route': 'dynamic',
#         'itemid' : itemid
#         }

#curl -X GET -i http://127.0.0.1:8000/item/1234
# 404 error:
# curl -X GET -i http://127.0.0.1:8000/item/my_item




@api.get('/item/{itemid:float}')
def get_item_float(itemid):
    return {
        'route': 'dynamic',
        'itemid': itemid,
        'source': 'float'
    }

@api.get('/item/{itemid}')
def get_item_default(itemid):
    return {
        'route': 'dynamic',
        'itemid': itemid,
        'source': 'string'
    }

#l'ordre dans lequel on définit les routes a une importance