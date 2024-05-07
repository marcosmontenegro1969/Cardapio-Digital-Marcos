def validar_cpf(cpf):
    # Remove . ou - se o usuario tiver colocado
    cpf = cpf.replace(".", "").replace("-", "")

    # Verifique se o CPF tem 11 digitos numéricos	
    if len(cpf) != 11 or not cpf.isdigit():
        return False

    # Verificação do primeiro dígito
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    if resto < 2:
        digito_verificador_1 = 0
    else:
        digito_verificador_1 = 11 - resto
    if int(cpf[9]) != digito_verificador_1:
        return False

    # Verificação do segundo dígito
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    if resto < 2:
        digito_verificador_2 = 0
    else:
        digito_verificador_2 = 11 - resto
    if int(cpf[10]) != digito_verificador_2:
        return False

    return True

while True:
    # Usuário informa o CPF
    cpf = input("Digite o seu CPF: ")

    # Validação do CPF
    if validar_cpf(cpf):
        print("CPF válido!")
        break
    else:
        print("CPF inválido!")
