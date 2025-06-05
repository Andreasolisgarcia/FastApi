# Installer Curl 

sudo apt-get update
sudo apt-get install curl 
curl -X GET https://jsonplaceholder.typicode.com/posts/1

# Installer Fast api + uvicorn (serveur de fastapi)

pip3 install fastapi httptools==0.1.* uvloop uvicorn
pip install fastapi uvicorn[standard]

Une fois que ce fichier est sauvegardé, lancez l'API dans une autre console en exécutant la commande suivante (ou si Si l'API ne tourne plus)

uvicorn fileName:api --reload

# Interfaces FastApi endpoints ( Documentation ):
- /docs
- /redoc
- /openapi.json

## Les librairies pour donner des types plus complexes à nos données.
- typing (module BaseModel)
- pydantic (modules Optional, List)