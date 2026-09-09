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
