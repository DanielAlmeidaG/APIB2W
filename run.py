from app import app

#Importando rotas
from app.routes import *

#Importando models
from app.models import planets

if __name__ == '__main__':
    app.run(port=8080, debug=True)