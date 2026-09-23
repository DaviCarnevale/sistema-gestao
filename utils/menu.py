def menu_principal():
    print("="*30)
    print("SISTEMA DE GESTÃO".center(30))
    print("="*30)
    print("\n1 - Clientes\n2 - Produtos\n3 - Vendas\n0 - Sair")
    opc = int(input("\nQual opção deseja escolher? "))
    return opc


def menu_clientes():
    print("="*30)
    print("CLIENTES".center(30))
    print("="*30)
    print("\n1 - Cadastrar\n2 - Listar\n3 - Buscar\n4 - Editar\n5 - Excluir\n0 - Voltar")
    opc = int(input("\nQual opção deseja escolher? "))
    return opc


def menu_produtos():
    print("="*30)
    print("PRODUTOS".center(30))
    print("="*30)
    print("\n1 - Cadastrar\n2 - Listar\n3 - Buscar\n4 - Editar\n5 - Excluir\n0 - Voltar")
    opc = int(input("\nQual opção deseja escolher? "))
    return opc
