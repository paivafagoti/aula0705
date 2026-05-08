from src.controller.filme_controller import FilmeController

filme = {
    "titulo": "Vingadores",
    "genero": "Ação",
    "diretor": "Marvel",
    "duracao": 120
}

controller = FilmeController()
controller.cadastrar(filme)
