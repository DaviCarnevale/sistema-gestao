from models import cliente
from services import cliente_service
from repositories import cliente_repository
import json

'''
cliente3 = cliente.Cliente(
    cpf="52348609819", 
    nome="Lucas",
    email="punish@gmail.com",
    cep="01000000",
    telefone="11993343535"
    )

c = cliente_service.ClienteService()
c.cadastrar(cliente3)   CADASTRA CLIENTES 
'''

# service = cliente_service.ClienteService() CHAMA O CLIENTE SERVICE

# service.editar(cpf="12345678909", campo="email", novo_valor="abc@gmail.com") EDITA DADOS DO CLIENTE

# service.excluir(cpf="12345678909") EXCLUI CLIENTE DE CLIENTES.JSON

# service.listar() LISTA OS CLIENTES

