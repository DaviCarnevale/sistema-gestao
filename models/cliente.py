class Cliente:
    def __init__(self, CPF: str, nome: str, email: str, telefone: str, CEP: str):
        self.__cpf = CPF
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.cep = CEP

    @property
    def cpf(self):
        return self.__cpf


cliente = Cliente(
    CPF="12345678900",
    nome="Davi Nunes",
    email="davi@email.com",
    telefone="11999999999",
    CEP="09500000"
)

print(cliente.nome)
print(cliente.cpf)
