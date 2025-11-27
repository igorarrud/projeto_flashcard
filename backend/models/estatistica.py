class estatistica():
    def __init__(self, id_usuario, id_flashcard, id_baralho, visualizacoes, vezes_de_novo = 0, vezes_facil = 0, vezes_medio = 0, vezes_dificil = 0,
                  ultima_revisao = None, ultima_resposta = None):
        self.id_usuario = id_usuario
        self.id_flashcard = id_flashcard
        self.id_baralho = id_baralho
        self.visualizacoes = visualizacoes
        self.vezes_de_novo = vezes_de_novo
        self.vezes_facil = vezes_facil
        self.vezes_medio = vezes_medio
        self.vezes_dificil = vezes_dificil
        self.ultima_revisao = ultima_revisao
        self.ultima_resposta = ultima_resposta

        
