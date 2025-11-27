from database.database import get_cursor

class flashcard_repository():
    def __init__(self, conexao):
        self.conn = conexao

    def criarFlashcard(self, nome_flashcard, pergunta, resposta, dificuldade):
        with get_cursor() as cursor:
            cursor.execute(
                "INSERT INTO Cartoes VALUES (%s, %s, %s, %s)", (nome_flashcard, pergunta, resposta, dificuldade)
            )

    # alterar status do flashcard no banco, método fundamental para retornar as estatísticas para o usuário
    def avaliarStatus(self, dificuldade):
        with get_cursor() as cursor:
            cursor.execute(
                "UPDATE Flashcards SET dificuldade = %s WHERE id = %s", (dificuldade, self.id)
            )
            return 1
