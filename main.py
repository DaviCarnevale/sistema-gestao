from models.cliente import Cliente
from models.produto import Produto
from services.produto_service import ProdutoService
from services.cliente_service import ClienteService
from utils.menu import (
    menu_principal,
    menu_clientes,
    menu_produtos
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
                try:
                    cpf = str(input("Digite o CPF do cliente que deseja excluir: "))
                    cliente = cliente_service.buscar(cpf=cpf)
                    cliente_service.exibir_cliente(cliente=cliente)
                    opc = int(input("Deseja excluir este cliente do sistema?\n1 - Sim\n0 - Não\n:"))
                    match opc:
                        case 1:
                            cliente_service.excluir(cpf=cpf)
                        case 0:
                            break
                        case _:
                            print("Opção inválida")
                except ValueError as erro:
                    print(erro)
            case 0:
                break
            case _:
                pass


def executar_menu_produtos():
    while True:
        opc = menu_produtos()
        match opc:
            case 1:
                try:
                    nome = str(input("Nome do produto: "))
                    preco = float(input("Preço: "))
                    estoque = int(input("Estoque: "))
                    produto_service.cadastrar(nome=nome, preco=preco, estoque=estoque)
                except ValueError as erro:
                    print(erro)
            case 2:
                produto_service.listar()
            case 3:
                try:
                    id = int(input("ID do produto: "))
                    produto = produto_service.buscar(id=id)
                    produto_service.exibir_produto(produto=produto)
                except ValueError as erro:
                    print(erro)
            case 4:
                try:
                    id_produto = int(input("Digite o ID do produto: "))
                    produto_service.buscar(id=id_produto)
                    while True:
                        print("\n1 - Nome\n2 - Preço\n3 - Estoque\n0 - Voltar")
                        opc = int(input("Selecione o campo que deseja mudar: "))
                        match opc:
                            case 1:
                                campo = "nome"
                                novo_valor = str(input("Digite o novo nome: "))
                            case 2:
                                campo = "preco"
                                novo_valor = float(input("Digite o novo preço: "))
                            case 3:
                                campo = "estoque"
                                novo_valor = int(input("Digite a nova quantidade no estoque: "))
                            case 0:
                                break
                            case _:
                                print("Opção inválida")
                                continue
                        produto_service.editar(id=id_produto, campo=campo, novo_valor=novo_valor)
                        break
                except ValueError as erro:
                    print(erro)
            case 5:
                try:
                    id_produto = int(input("Digite o ID do produto que deseja excluir: "))
                    produto = produto_service.buscar(id=id_produto)
                    produto_service.exibir_produto(produto=produto)
                    opc = int(input("Deseja excluir este produto do sistema?\n1 - Sim\n0 - Não\n:"))
                    match opc:
                        case 1:
                            produto_service.excluir(id=id_produto)
                        case 0:
                            break
                        case _:
                            print("Opção inválida")
                except ValueError as erro:
                    print(erro)
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
            executar_menu_produtos()
        case 3:
            pass
        case 0:
            break
        case _:
            pass




# PRODUTOS

# service = ProdutoService()

# service.cadastrar("Mouse Gamer", 150.00, 20) CADASTRA UM PRODUTO

# service.editar(id=produto.id, campo="preco", novo_valor=120) EDITA UM PRODUTO

# service.excluir(id=8757) EXCLUI UM PRODUTO

# service.listar() LISTA OS PRODUTOS
