from models import cliente

cliente = cliente.Cliente(
    CPF="12345678909",
    nome="Davi Nunes",
    email="davi@email.com",
    telefone="11999999999",
    CEP="09500000"
)

print(cliente.nome)
print(cliente.cpf)
