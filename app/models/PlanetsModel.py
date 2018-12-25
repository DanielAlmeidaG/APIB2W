from flask_restful import Api, Resource, reqparse
from app.database import dbController

class Planet(Resource):
    #inicializando o controller do banco de dados dentro do model
    def __init__(self):
        self.db = dbController.Controller()

    #definindo os gets
    def get(self, name):
        #busca o determinado planeta no banco de dados
        planets  = self.db.get(name)

        #caso retorne algo diferente de false significa que retornou algum planeta
        if(planets):
            ret = []
            for planet in planets:
                #insere no retorno todos os planetas(será mais de um caso tenha sido pesquisado '*')
                ret.append({
                    "id": planet[0],
                    "nome": planet[1],
                    "clima": planet[2],
                    "terreno": planet[3],
                    "aparicoes": planet[4]
                })
            return ret, 200

        #caso nao retorne planeta algum, indica que o planeta não foi encontrado no bd
        return "Planeta não encontrado", 404


    #definindo os sets
    def post(self, name):
        #verifica se o planeta já não existe na base de dados
        if(self.get(name)[1] == 200):
            return "Planeta {} já está cadastrado".format(name), 400

        #caso não, coleta os dados inseridos por um json
        parser = reqparse.RequestParser()
        parser.add_argument("clima")
        parser.add_argument("terreno")
        parser.add_argument("aparicoes")
        args = parser.parse_args()

        #cria um planeta nas formas corretas
        planet = {
                "nome": name,
                "clima": args["clima"],
                "terreno": args["terreno"],
                "aparicoes": args["aparicoes"]
            }
        
        #insere no banco de dados e retorna o planeta
        self.db.set(planet)
        return self.get(name)[0], 201
    
    #definindo a remoção
    def delete(self, name):
        #verifica se de fato existe um planeta com esse nome ou id no banco de dados
        planet = self.get(name)
        if(planet[1] != 200):
            #caso o status não seja o de "encontrado", indica o erro
            return "O planeta não está cadastrado", 400

        #deleta o planeta do banco de dados e indica que o planeta foi removido
        self.db.delete(name)
        return "O planeta {} foi deletado".format(planet[0][0]['nome']), 200