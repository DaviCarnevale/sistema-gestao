from utils.validacoes import (
    validar_cpf, 
    validar_nome, 
    validar_email, 
    validar_telefone, 
    validar_cep
    )

class Cliente:
    def __init__(self, cpf: str, nome: str, email: str, telefone: str, cep: str):
        validacoes = [
            (validar_cpf, cpf, "CPF"),
            (validar_nome, nome, "nome"),
            (validar_email, email, "email"),
            (validar_telefone, telefone, "telefone"),
            (validar_cep, cep, "CEP")
        ]
        for funcao, dado, nome_campo in validacoes:
            resultado = funcao(dado)
            if not resultado:
                raise ValueError(f"{nome_campo} é inválido")

        self.__cpf = cpf
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.cep = cep

    @property
    def cpf(self):
        return self.__cpf

