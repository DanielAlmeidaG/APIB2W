import json, requests
from app.database import dbController


class ExtApi():
    def __init__(self):
        #acessa o link disponibilizado da api
        response = requests.get("https://swapi.co/api/planets/")
        comments = json.loads(response.content)
        
        #instancia o controlador do banco de dados
        db = dbController.Controller()

        for planetAPI in comments['results']:
            #para todos os planetas do resultado da API é criado uma especie de 'subplaneta' com os dados relevantes
            planet = {
                "nome": planetAPI['name'],
                "clima": planetAPI['climate'],
                "terreno": planetAPI['terrain'],
                "aparicoes": str(planetAPI['films'])
            }
            #insere no banco de dados o 'subplaneta'
            db.set(planet)