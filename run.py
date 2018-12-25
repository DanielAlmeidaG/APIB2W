from flask import Flask
from flask_restful import Api, Resource, reqparse
from app.models import PlanetsModel
from app import extApi

#iniciando
app = Flask(__name__)
api = Api(app)

#buscando planetas da api disponibilizada
extApi.ExtApi()

#criando as rotas
api.add_resource(PlanetsModel.Planet, "/planet/<string:name>")

#rodando o programa
app.run(debug=True)
