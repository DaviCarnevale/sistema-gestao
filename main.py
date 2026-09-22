from models.cliente import Cliente
from services.produto_service import ProdutoService
from services.cliente_service import ClienteService
from utils.menu import (
    menu_principal,
    menu_clientes
    )

cliente_service = ClienteService()
produto_service = ProdutoService()

def executar_menu_clientes():
    while True:
        opc = menu_clientes()
        match opc:
            case 1:
                try:
                    cpf = str(input("CPF: "))
                    nome = str(input("Nome: "))
                    email = str(input("Email: "))
                    telefone = str(input("Número de telefone: "))
                    cep = str(input("CEP: "))
                    c = Cliente(cpf=cpf, nome=nome, email=email, telefone=telefone, cep=cep)
                    cliente_service.cadastrar(cliente=c)
                except ValueError as erro:
                    print(erro)
            case 2:
                cliente_service.listar()
            case 3:
                try:
                    cpf = str(input("CPF: "))
                    cliente = cliente_service.buscar(cpf)
                    cliente_service.exibir_cliente(cliente)
                except ValueError as erro:
                    print(erro)
            case 4:
                try:
                    cpf = str(input("CPF: "))
                    cliente_service.buscar(cpf=cpf)
                    while True:
                        print("\n1 - Nome\n2 - Email\n3 - Telefone\n4 - CEP\n0 - Voltar")
                        opc = int(input("Selecione o campo que deseja editar: "))
                        match opc:
                            case 1:
                                campo = "nome"
                            case 2:
                                campo = "email"
                            case 3:
                                campo = "telefone"
                            case 4:
                                campo = "cep"
                            case 0:
                                break
                            case _:
                                print("Opção inválida")
                                continue
                        novo_valor = str(input(f"Digite o novo {campo}: "))
                        cliente_service.editar(cpf=cpf, campo=campo, novo_valor=novo_valor)
                        break
                except ValueError as erro:
                    print(erro)
            case 5:
                cpf = str(input("Digite o CPF do cliente que deseja excluir: "))
                cliente_service.excluir(cpf=cpf)
            case 0:
                break
            case _:
                pass

while True:
    opc = menu_principal()

    match opc:
        case 1:
            executar_menu_clientes()
        case 2:
            pass
        case 3:
            pass
        case 0:
            break
        case _:
            pass



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
