from utils.validacoes import (
    validar_nome_produto,
    validar_preco,
    validar_estoque
)


class Produto:

    def __init__(self, id, nome, preco, estoque):
        validacoes = [
            (validar_nome_produto, nome, "nome"),
            (validar_preco, preco, "preço"),
            (validar_estoque, estoque, "estoque")
        ]
        for funcao, dado, nome_campo in validacoes:
            resultado = funcao(dado)
            if not resultado:
                raise ValueError(f"{nome_campo} é inválido")

        self.__id = id
        self.nome = nome
        self.preco = preco
        self.estoque = estoque


    @property
    def id(self):
        return self.__id

