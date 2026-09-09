from utils.validacoes import validar_cpf

class Cliente:
    def __init__(self, CPF: str, nome: str, email: str, telefone: str, CEP: str):
        if validar_cpf(CPF):
            self.__cpf = CPF
        else:
            raise ValueError("O CPF digitado é inválido")
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.cep = CEP

    @property
    def cpf(self):
        return self.__cpf

