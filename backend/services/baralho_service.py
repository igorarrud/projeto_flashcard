class baralho_service():
    def __init__(self, repo):
        self.repo = repo

    """ 
    optei por não apagar os dados do banco caso o usuário apague o baralho, ao invés disso, o baralho ficará em estado desativado,
    se usuário baixar de novo, não perde o histórico, a parte de desativar, é para não atrapalhar na hora de retornar estatísticas e retornar estatísticas de um baralho desativado
    """
    def desativar_baralho_service(self, id_usuario, id_baralho):
        baralho = self.repo.buscar_baralho(id_usuario, id_baralho)

        if not baralho:
            raise ValueError("Baralho não encontrado para o usuário")

        self.repo.desativar_baralho_repo(id_baralho)

    def editar_baralho(self, id_usuario, id_baralho, acao, dados):
        baralho = self.repo.buscar_baralho(id_usuario, id_baralho)

        if not baralho:
            raise ValueError("Baralho não encontrado para o usuário")
        
        if acao == "alterar_info":
            return self._alterar_dados(baralho, dados)
        
        elif acao == "adicionar_flashcard":
            return self._adicionar_flashcard(baralho, dados)
        
        elif acao == "remover_flashcard":
            return self._remover_flashcard(baralho, dados)
        
        else:
            raise ValueError("Ação inválida")


# validar se o baralho existe
# verificar se o flashcard que estou adicionando existe
# seria interessante uma mensagem para mostrar que o flashcard que o usuario está adicionando não pertence a categoria do baralho