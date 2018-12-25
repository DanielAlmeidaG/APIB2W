import sqlite3

class Controller():
    def get(self, name):     
        #abre o banco de dados   
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()

        #verifica se o usuario deseja todos os planetas ou um especifico
        if(name == "*"):
            #retorna todos os planetas do BD
            self.cursor.execute("""SELECT * FROM Planets""")
        else:    
            #primeiro tenta converter o 'nome' para inteiro, para poder pesquisar por id
            try:
                self.cursor.execute("""SELECT * FROM Planets WHERE id=?""", (int(name),))
            #caso não consiga pesquisa por nome
            except:
                self.cursor.execute("""SELECT * FROM Planets WHERE nome=?""", (name,))

        #insere no retorno os dados que foram retornados do banco
        ret = self.cursor.fetchall()

        #fecha o banco de dados
        self.conn.close()

        if(ret == []):
            #caso o retorno seja vazio, significa que nada foi encontrado, logo retorna falso
            return False
        else:
            #caso não seja vazio, retorna o proprio retorno do BD
            return ret

    def set(self, planet):
        #primeiro verifica se já existe algum planeta com esse nome, caso sim. Não permite a inserção
        if(self.get(planet['nome']) != False):
            return

        #abre o banco de dados   
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()

        #executa a inserção no banco
        self.cursor.execute("""INSERT INTO Planets (nome, clima, terreno, aparicoes) VALUES 
        (?,?,?,?)""", (planet['nome'], planet['clima'], planet['terreno'], planet['aparicoes']))

        #atualiza o banco e o fecha
        self.conn.commit()
        self.conn.close()
        return

    def delete(self, name):
        #pesquisa se de fato existe algum planeta com esse nome ou id
        if(self.get(name) == False):
            return

        #abre o banco de dados   
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()

        try:
            #primeiro tenta converter o 'nome' para inteiro, para poder pesquisar por id
            self.cursor.execute("""DELETE FROM Planets WHERE id = ?""", (int(name),))
        except:
            #caso não consiga pesquisa por nome
            self.cursor.execute("""DELETE FROM Planets WHERE nome = ?""", (name,))

        #atualiza o banco e o fecha
        self.conn.commit()
        self.conn.close()
        return