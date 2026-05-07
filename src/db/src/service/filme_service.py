class FilmeService:

    def validar(self, filme):

        if filme["titulo"] == "":
            raise Exception("Título obrigatório")

        return True
