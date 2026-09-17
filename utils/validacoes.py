# VALIDAÇÕES PARA CLIENTES

def validar_cpf(cpf) -> bool:
    if len(cpf) == 11 and cpf.isdigit():
        if cpf == cpf[0] * 11:
            return False
        soma_1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
        resto_1 = soma_1 % 11
        digito_1 = 0 if resto_1 < 2 else 11 - resto_1

        soma_2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
        resto_2 = soma_2 % 11
        digito_2 = 0 if resto_2 < 2 else 11 - resto_2
        return int(cpf[9]) == digito_1 and int(cpf[10]) == digito_2
    else: 
        return False


def validar_nome(nome: str) -> bool:
    return len(nome.strip()) >= 3 and not any(
        char.isdigit() for char in nome.strip()
    )


def validar_email(email: str) -> bool:
    if email.count("@") != 1:
        return False
    usuario, dominio = email.split("@")
    usuario = usuario.strip()
    dominio = dominio.strip()
    return len(usuario) >= 3 and len(dominio) >= 3 and "." in dominio


def validar_telefone(num_telefone: str) -> bool:
    return (len(num_telefone) == 11 
            and num_telefone.isdigit() 
            and num_telefone != num_telefone[0] * 11
    )


def validar_cep(cep: str) -> bool:
    return (len(cep) == 8 
            and cep.isdigit()
            and cep != cep[0] * 8
    )


# VALIDAÇÕES PARA PRODUTOS

def validar_nome_produto(nome: str):
    return len(nome.strip()) >= 3 and any(char.isalpha() for char in nome)


def validar_preco(preco: float):
    return isinstance(preco, (float, int)) and preco >= 0.01


def validar_estoque(qtd: int):
    return isinstance(qtd, int) and qtd >= 0

