# pip install fastapi
pip install -r requirements.txt
# pip install uvicorn
# pip3 install jinja2   from fastapi.templating import Jinja2Templates
# pip3 install aiofiles pour le css
# pip install sqlalchemy for bd
utiliser pour lancer le serveur
uvicorn run:app --reload(pour lancer automatiquement quand le serveur est pret)

# pip install pydantic
Pydantic = validation + typage + transformation automatique des données.
c'est le coeur de la validation des données. sans lui fastapi n'est rien

# Windows
python -m venv venv
venv\Scripts\activate

Types supportés
Pydantic comprend :
str,int,float,bool,list,dict,datetime,EmailStr,HttpUrl

# pip install fastapi uvicorn
pip list

# swagger 
Swagger est un outil de documentation automatique d’API REST. c'est l'interface graphique permettant
de texter les enpoints
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc  interface plus propre
http://127.0.0.1:8000/openapi.json

app = FastAPI(docs_url=None, redoc_url=None)
desactiver en production

auth 3H36 posgress sql root

uvicorn main:app --reload