import mysql.connector
from contextlib import contextmanager

conexao = {
        "host": "localhost",
        "user": "root",
        "password": "",
        "database": "Flashcards"
}   

def get_connection():
    return mysql.connector.connect(**conexao)

@contextmanager
def get_cursor():
        conn = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            yield cursor
            conn.commit()
        except Exception as e:
            if conn:
                conn.rollback()
            raise e
        finally:
            if conn:
                conn.close()
