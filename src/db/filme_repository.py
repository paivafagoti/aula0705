class FilmeRepository:

    def salvar(self, conexao, filme):

        cursor = conexao.cursor()

        sql = """
        INSERT INTO filme(titulo, genero, diretor, duracao)
        VALUES (?, ?, ?, ?)
        """

        cursor.execute(sql, (
            filme["titulo"],
            filme["genero"],
            filme["diretor"],
            filme["duracao"]
        ))

        conexao.commit()
