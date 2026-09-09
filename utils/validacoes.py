def validar_cpf(cpf) -> bool:
    return len(cpf) == 11 and cpf.isdigit()
