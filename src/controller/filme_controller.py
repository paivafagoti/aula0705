from src.db.database import conectar
from src.repository.filme_repository import FilmeRepository
from src.service.filme_service import FilmeService

class FilmeController:

    def cadastrar(self, filme):

        conexao = conectar()

        service = FilmeService()
        repository = FilmeRepository()

        service.validar(filme)

        repository.salvar(conexao, filme)

        print("Filme cadastrado com sucesso")
