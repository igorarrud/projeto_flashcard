from database.database import get_cursor
from models.estatistica import estatistica

"""
tem que criar os métodos que o service está utilizando
"""

class estatistica_repository():
    def __init__(self, conexao):
        self.conn = conexao

    def converter_tuplas_em_entidades(self, row):
        return estatistica(id_usuario=row[0],
                           id_flashcard=row[1],
                           id_baralho=row[2],
                           visualizacoes=row[3],
                           vezes_de_novo=row[4],
                           vezes_facil=row[5],
                           vezes_medio=row[6],
                           vezes_dificil=row[7],
                           ultima_revisao=row[8],
                           ultima_resposta=row[9])


    # deve ser definido que um flashcard não pode fazer parte de mais um baralho, já é um regra de negócio que não pode haver flashcards duplicados,
    # portanto, o método abaixo quebraria se um flashcard fosse membro de mais de um baralho, fazer validação para impedir isso
    def buscar_estatistica(self, id_usuario, id_flashcard, id_baralho):
        with get_cursor() as cursor:
            cursor.execute(
                "SELECT id_usuario, id_flashcard, id_baralho, visualizacoes,  \
                vezes_de_novo, vezes_facil, vezes_medio, vezes_dificil, ultima_revisao, ultima_resposta FROM Estatistica WHERE id_usuario = %s id_flashcard = %s id_baralho = %s", 
                (id_usuario, id_flashcard, id_baralho)
            )

            # fetchone retorna tupla
            row = cursor.fetchone()

        if row is None:
            return None

        return self.converter_tuplas_em_entidades(row)
    
    def criar_estatistica_repo(self, id_usuario, id_flashcard, id_baralho):
        with get_cursor() as cursor:
            cursor.execute(
                "INSERT INTO Estatistica (id_usuario, id_flashcard, id_baralho, visualizacoes, vezes_de_novo, vezes_facil, vezes_medio, vezes_dificil, ultima_revisao, ultima_resposta) " \
                "VALUES (%s, %s, %s, 0, 0, 0, 0, 0, NULL, NULL)", (id_usuario, id_flashcard, id_baralho)
            )

    # esse método é parecido com o buscar_estatistica, porém ele retorna mais de uma linha, o que é fundamental para construir relatórios em outros métodos
    def buscar_estatisticas_baralho(self, id_usuario, id_baralho):
        with get_cursor() as cursor:
            cursor.execute(
                "SELECT id_usuario, id_flashcard, id_baralho, visualizacoes,  \
                vezes_de_novo, vezes_facil, vezes_medio, vezes_dificil, ultima_revisao, ultima_resposta FROM Estatistica WHERE id_usuario = %s AND id_baralho = %s", 
                (id_usuario, id_baralho)
            )
            
            rows = cursor.fetchall()

            # Lista de tuplas
            return [self.converter_tuplas_em_entidades(row) for row in rows] if rows else None
        
    # esse método seleciona os flashcards ativos, ele une a tabela estatisticas e baralho para retornar apenas as estatísticas de flashcards que pertencem a baralhos ativos
    def buscar_estatisticas_flashcard(self, id_usuario):
        with get_cursor as cursor:
            cursor.execute(
                "SELECT e.id_usuario, e.id_flashcard, e.id_baralho, e.visualizacoes," \
                " e.vezes_de_novo, e.vezes_facil, e.vezes_medio, e.vezes_dificil, e.ultima_revisao, e.ultima_resposta" \
                " FROM Estatistica e JOIN Baralho b ON b.id_baralho = e.id_baralho" \
                " WHERE e.id_usuario = %s AND b.ativo = 1", (id_usuario,)
            )

            rows = cursor.fetchall()

            return [self.converter_tuplas_em_entidades(row) for row in rows] if rows else None
        