from database import get_cursor

class flashcard():
    def __init__(self, id_flashcard, id_baralho,pergunta, resposta, dificuldade):
        self.id_flashcard = id_flashcard
        self.id_baralho = id_baralho
        self.pergunta = pergunta
        self.resposta = resposta
        self.dificuldade = dificuldade

    def exibirResposta(self):
        return self.resposta
