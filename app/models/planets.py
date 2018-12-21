from app import db
from app import manager

class Planeta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True)
    clima = db.Column(db.String(100))
    terreno = db.Column(db.String(100))
    aparicoes = db.Column(db.Integer)

db.create_all()
manager.create_api(Planeta, methods=['POST', 'GET', 'PUT', 'DELETE'])