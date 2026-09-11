from models import cliente
from services import cliente_service

cliente1 = cliente.Cliente(
    cpf="12345678909",
    nome="Davi Nunes",
    email="davi@email.com",
    telefone="11999999999",
    cep="09500000"
)

cliente2 = cliente.Cliente(
    cpf="16362732898",
    nome="Davi Nunes",
    email="davi@email.com",
    telefone="11999999999",
    cep="09500000"
)

service = cliente_service.ClienteService()

service.cadastrar(cliente1)
service.cadastrar(cliente2)

service.listar()

service.editar(cpf="16362732898", campo="cep", novo_valor="09531160")

service.excluir(cpf="1636273898")

service.listar()
