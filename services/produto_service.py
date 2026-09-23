from random import choice
from repositories.produto_repository import (salvar_produtos, carregar_produtos)
from models.produto import Produto
from utils.validacoes import (
    validar_nome_produto,
    validar_preco,
    validar_estoque
)

class ProdutoService:

    def __init__(self):
        self.produtos = carregar_produtos()

    def gerar_id(self):
            ids_existentes = {p.id for p in self.produtos}
            ids_disponiveis = set(range(1000, 10000)) - ids_existentes
            if not ids_disponiveis:
                raise IndexError("O número máximo de id's foi atingido")
            return choice(list(ids_disponiveis))


    def cadastrar(self, nome: str, preco, estoque: int):
        id = self.gerar_id()
        p = Produto(id, nome, preco, estoque)
        self.produtos.append(p)
        salvar_produtos(self.produtos)


    def listar(self):
         for produto in self.produtos:
            informacoes = [
                ("id", produto.id),
                ("nome", produto.nome),
                ("preço", produto.preco),
                ("estoque", produto.estoque)
            ]
            for informacao, dado in informacoes:
                print(f"{informacao}: {dado}")
            print("-"*20)


    def buscar(self, id: int):
        for p in self.produtos:
            if p.id == id:
                return p
        raise ValueError("Produto não encontrado")


    def exibir_produto(self, produto):
        informacoes = [
            ("id", produto.id),
            ("nome", produto.nome),
            ("preço", produto.preco),
            ("estoque", produto.estoque)
        ]
        for informacao, dado in informacoes:
            print(f"{informacao}: {dado}")
        print("-"*20)


    def editar(self, id: int, campo: str, novo_valor):
        p = self.buscar(id)
        validacoes = [
            (validar_nome_produto, "nome"),
            (validar_preco, "preco"),
            (validar_estoque, "estoque")
        ]
        for funcao, nome_campo in validacoes:
            if nome_campo == campo:
                resultado = funcao(novo_valor)
                if not resultado:
                    raise ValueError(f"{campo} é inválido")
                setattr(p, campo, novo_valor)
                salvar_produtos(self.produtos)
                print(f"{campo} alterado com sucesso")
                break
        else:
            raise ValueError(f"{campo} é inválido")


    def excluir(self, id: int):
        p = self.buscar(id)
        self.produtos.remove(p)
        salvar_produtos(self.produtos)
            