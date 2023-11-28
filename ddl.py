import sqlite3

conn = sqlite3.connect('escola.db')

cursor = conn.cursor()


cursor.execute(
    """
        create tb_estudante(
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               nome VARCHAR(200) NOT NULL,
               email TEXT NOT NULL,
               MATRICULA TEXT NOT NULL    
        )
               
    """
)

print('CRIADO COM SUCESSO')