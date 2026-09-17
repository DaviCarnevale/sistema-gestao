from random import choice, randint

class ProdutoService:

    def __init__(self):
        self.produtos = []

    def gerar_id(self):
            ids_existentes = {p.id for p in self.produtos}
            ids_disponiveis = set(range(1000, 10000)) - ids_existentes
            if not ids_disponiveis:
                raise IndexError("O número máximo de id's foi atingido")
            return choice(list(ids_disponiveis))

