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
