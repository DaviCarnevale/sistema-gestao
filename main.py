from models import cliente
from services import cliente_service
from repositories import cliente_repository
import json

cliente1 = cliente.Cliente(
        cpf="52998224725",
        nome="Davi",
        email="davi@email.com",
        telefone="11999999999",
        cep="09500000"
)
cliente2 = cliente.Cliente(
        cpf="12345678909",
        nome="João",
        email="joao@email.com",
        telefone="11988888888",
        cep="01001000"
)


cliente_repository.salvar_clientes(clientes=[cliente1, cliente2])

print(cliente_repository.carregar_clientes())