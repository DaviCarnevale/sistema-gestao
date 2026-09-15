from utils.validacoes import (
    validar_nome, 
    validar_email, 
    validar_telefone, 
    validar_cep
)

from repositories import cliente_repository


class ClienteService:

    def __init__(self):
        self.clientes = []


    def cadastrar(self, cliente):
        for cliente_existente in self.clientes:
            if cliente.cpf == cliente_existente.cpf:
                raise ValueError("Este CPF já está cadastrado no sistema")
        self.clientes.append(cliente)


    def listar(self):
        for cliente in self.clientes:
            informacoes = [
                ("CPF", cliente.cpf),
                ("Nome", cliente.nome),
                ("Email", cliente.email),
                ("Telefone", cliente.telefone),
                ("CEP", cliente.cep)
            ]
            for informacao, dado in informacoes:
                print(f"{informacao}: {dado}")
            print("-"*20)


    def buscar(self, cpf: str):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        raise ValueError("Cliente não encontrado")


    def editar(self, cpf: str, campo: str, novo_valor: str):
        cliente = self.buscar(cpf)
        validacoes = [
            (validar_nome, "nome"),
            (validar_email, "email"),
            (validar_telefone, "telefone"),
            (validar_cep, "cep")
        ]
        for funcao, nome_campo in validacoes:
            if nome_campo == campo:
                resultado = funcao(novo_valor)
                if not resultado:
                    raise ValueError(f"{campo} é inválido")
                setattr(cliente, campo, novo_valor)
                print(f"{campo} alterado com sucesso")
                break
        else:
            raise ValueError(f"{campo} é inválido")


    def excluir(self, cpf: str):
        cliente = self.buscar(cpf)
        self.clientes.remove(cliente)
        