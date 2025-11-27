from database.database import get_cursor
from models.baralho import baralho

class baralho_repository():
    def __init__(self, conexao):
        self.conn = conexao

    def converter_tupla_em_entidade(self, row):
        return baralho(id_baralho=row[0],
                       nome=row[1],
                       categoria=row[2],
                       ativo=row[3])

    def criarBaralho(self, nome_baralho, categoria):
        with get_cursor() as cursor:
            cursor.execute(
                "INSERT INTO baralhos (id_usuario, nome_baralho, categoria) VALUES (%s, %s,%s)",
                (self.id, nome_baralho, categoria)
            )

    def adicionarFlashcard(self, id_baralho, id_flashcard):
        ...

    def removerFlashcard(self, id_baralho, id_flashcard):
        ...

    def buscar_baralho(self, id_baralho):
        with get_cursor() as cursor:
            cursor.execute(
                "SELECT * FROM Baralho WHERE id_baralho = %s", (id_baralho,)
            )

            row = cursor.fetchone()

        if row is None:
            return None
        
        return self.converter_tupla_em_entidade(row) if row else None

    def desativar_baralho_repo(self, id_baralho):
        with get_cursor() as cursor:
            cursor.execute(
                "UPDATE Baralho SET ativo = 0 WHERE id_baralho = %s", (id_baralho)
            )

