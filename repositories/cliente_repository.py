from models import cliente
import json

def cliente_para_dict(cliente):
    return {
        "cpf": cliente.cpf,
        "nome": cliente.nome,
        "email": cliente.email,
        "telefone": cliente.telefone,
        "cep": cliente.cep
    }


def dict_para_cliente(dados):
    return cliente.Cliente(**dados)


def salvar_clientes(clientes):
    dados = [
        cliente_para_dict(cliente) 
        for cliente in clientes
    ]
    with open ("data/clientes.json", "w", encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


def carregar_clientes():
    try:
        with open ("data/clientes.json", "r", encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
        clientes = [
            dict_para_cliente(dado)
            for dado in dados
        ]
        return clientes
    except json.decoder.JSONDecodeError:
        return []
    except FileNotFoundError:
        clientes = []
        with open("data/clientes.json", "w", encoding='utf-8') as arquivo:
            json.dump(clientes, arquivo, indent=4, ensure_ascii=False)
        return clientes