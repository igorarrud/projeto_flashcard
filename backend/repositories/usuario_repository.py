from database.database import get_cursor

class usuario_repository():
    def __init__(self, conexao):
        self.conn = conexao