import datetime
from repositories import baralho_repository

class estatistica_service():
    def __init__(self, estat_repo, baralho_repo):
        self.repo = estat_repo
        self.baralho_repo = baralho_repo

    def registrar_resposta(self, id_usuario, id_flashcard, id_baralho, resposta):
        '''
        estat é uma instância do model estatistica, o método buscar retorna um model estatistica, o model utiliza do service e o service usa o repositório para a lógica ser feita
        '''
        estat = self.repo.buscar_estatistica(id_usuario, id_flashcard, id_baralho)

        # método preventivo, provavelmente, nunca vai acontecer essa situação, pois ao usuário adicionar o baralho em sua biblioteca, as estatísticas já serão criadas
        if estat is None:
            # se for None, registra a resposta de agora no banco
            estat = self.repo.criar_estatistica(id_usuario, id_flashcard, id_baralho)

            estat.visualizacoes += 1
            estat.ultima_resposta = resposta
            estat.ultima_revisao = datetime.now()
        else:
            estat.visualizacoes += 1

        if resposta == "de novo":
            estat.vezes_de_novo += 1
        elif resposta == "fácil":
            estat.vezes_facil += 1
        elif resposta == "médio":
            estat.vezes_medio += 1
        elif resposta == "difícil":
            estat.vezes_dificil += 1
        else:
            print("tem algum erro no código ai kkkkkkkk")

        self.repo.salvar_estatistica(estat)


    """
    criei dois métodos de criar estatística, um para o service, pois é necessário validação (repositório não pode fazer isso) e um para o repositório
    o do service verificar se existe, se existe retorna um erro, se não chama o criar do repositório para criar
    o criar do repositório apenas executa, ele cria sem lógica alguma
    """
    def criar_estatistica_service(self, id_usuario, id_flashcard, id_baralho):
        existe = self.repo.buscar_estatistica(id_usuario, id_flashcard, id_baralho)

        if existe:
            raise ValueError("Estatística para esse usuário já existe")
        
        self.repo.criar_estatistica_repo(id_usuario, id_flashcard, id_baralho)

    # três validações, verificar se baralho existe, se está ativo e se há estatísticas para ele
    def retornar_estatistica_baralho_em_entidade(self, id_usuario, id_baralho):
        baralho = self.baralho_repo.buscar_baralho(id_usuario, id_baralho)

        # condição preventiva
        if not baralho:
            raise ValueError("Baralho não encontrado para esse usuário")
        
        # condição preventiva
        if not baralho.ativo:
            return None

        estat = self.repo.buscar_estatistica_baralho(id_usuario, id_baralho)

        # condição preventiva
        if not estat:
            return []
        
        # filtro de dados
        estatisticas = [
            e for e in estat if e.visualizacoes > 0
        ]

        return estatisticas

    # três validações, verificar se o flashcard existe, verificar se o baralho a qual ele pertence está ativo e se há estatísticas para ele
    def retornar_estatistica_flashcard_em_entidade(self, id_usuario):
        estat = self.repo.buscar_estatistica_flashcard(id_usuario)

        if not estat:
            return []

        return estat

    # buscar_estatisticas_baralho faz algo similar, a ideia desse era dar uma visão mais geral do baralho, quantidade de flashcards dominados, quantidades de vezes que praticou
    # implementar se der tempo
    def avaliarDesempenhoBaralho(self, id_baralho):
        pass