from database.database import get_cursor

class usuario_repository():
    def __init__(self, conexao):
        # conectar ao banco
        self.conn = conexao

    # consertar o return dos métodos abaixo, não devem retornar o cursor


    @staticmethod
    def criarBaralho(self, nome_baralho, categoria):
        with get_cursor() as cursor:
            cursor.execute(
                "INSERT INTO baralhos (id_usuario, nome_baralho, categoria) VALUES (%s, %s,%s)",
                (self.id, nome_baralho, categoria)
            )
            return {"sucesso": True, "id": cursor.lastrowid}
        
    @staticmethod
    def criarFlashcard(self, nome_flashcard, pergunta, resposta, dificuldade):
        with get_cursor() as cursor:
            cursor.execute(
                "INSERT INTO Cartoes VALUES (%s, %s, %s, %s)", (nome_flashcard, pergunta, resposta, dificuldade)
            )
            return {"sucesso":True, "id":cursor.lastrowid}
            