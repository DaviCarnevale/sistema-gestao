from models.cliente import Cliente
from services.produto_service import ProdutoService
from services.cliente_service import ClienteService
from repositories.cliente_repository import carregar_clientes

# CLIENTES

'''
cliente3 = Cliente(
    cpf="52348609819", 
    nome="Lucas",
    email="punish@gmail.com",
    cep="01000000",
    telefone="11993343535"
    )

c = ClienteService()
c.cadastrar(cliente3)   CADASTRA CLIENTES 
'''

# service = ClienteService() CHAMA O CLIENTE SERVICE

# service.editar(cpf="12345678909", campo="email", novo_valor="abc@gmail.com") EDITA DADOS DO CLIENTE

# service.excluir(cpf="12345678909") EXCLUI CLIENTE DE CLIENTES.JSON

# service.listar() LISTA OS CLIENTES

# carregar_clientes()


# PRODUTOS

# service = ProdutoService()

# service.cadastrar("Mouse Gamer", 150.00, 20) CADASTRA UM PRODUTO

# service.editar(id=produto.id, campo="preco", novo_valor=120) EDITA UM PRODUTO

# service.excluir(id=8757) EXCLUI UM PRODUTO

# service.listar() LISTA OS PRODUTOS
