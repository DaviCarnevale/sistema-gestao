from models.produto import Produto
import json

def produto_para_dict(produto):
    return {
        "id": produto.id,
        "nome": produto.nome,
        "preco": produto.preco,
        "estoque": produto.estoque
    }


def dict_para_produto(dados):
    return Produto(**dados)


def salvar_produtos(produtos):
    dados = [
        produto_para_dict(produto)
        for produto in produtos
    ]
    with open ("data/produtos.json", "w", encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


def carregar_produtos():
    try:
        with open ("data/produtos.json", "r", encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
        produtos = [
            dict_para_produto(dado)
            for dado in dados
        ]
        return produtos
    except json.decoder.JSONDecodeError:
        return []
    except FileNotFoundError:
        produtos = []
        with open ("data/produtos.json", "w", encoding='utf-8') as arquivo:
            json.dump(produtos, arquivo, indent=4, ensure_ascii=False)
        return produtos
