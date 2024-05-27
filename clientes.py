import os
import time
from Idioma_navegacao import get_mensagem_navegacao  # Função para obter mensagens de navegação
from pratos import escolhe_cardapio  # Função para escolher cardápio

def efetua_login(idioma_atual, mostra_tela_titulo, rotina_em_desenvolvimento, bemvindo):
    # Função auxiliar para buscar a senha associada a um email
    def busca_senha_por_email(email):
        caminho_arquivo = "../CARDAPIO.MARCOS/txt/clientes.txt"  # Caminho do arquivo de clientes
        with open(caminho_arquivo, mode='r', encoding='utf-8') as file:
            for line in file:
                dados = line.strip().split(',')
                if dados[1] == email:
                    return dados[2]
        return None

    mostra_tela_titulo()

    # Loop para obter um email válido do usuário
    while True:
        email = input(f"\n{get_mensagem_navegacao(idioma_atual, 'informe_seu_email')}")
        
        if email == "":
            return
        
        if valida_email(email):
            break
        else:
            print(f"\n{get_mensagem_navegacao(idioma_atual, 'email_invalido')}")

    senha_armazenada = busca_senha_por_email(email)
    if senha_armazenada:
        senha = input(get_mensagem_navegacao(idioma_atual, 'informe_senha'))
        if senha == senha_armazenada:
            print(get_mensagem_navegacao(idioma_atual, 'login_sucesso'))
            global logado
            logado = True
            time.sleep(2)
            escolhe_cardapio(idioma_atual, mostra_tela_titulo, rotina_em_desenvolvimento, bemvindo)
        else:
            print(get_mensagem_navegacao(idioma_atual, 'login_falhou'))
            time.sleep(2)
            efetua_login(idioma_atual, mostra_tela_titulo, rotina_em_desenvolvimento, bemvindo)
    else:
        print(get_mensagem_navegacao(idioma_atual, 'email_nao_encontrado'))
        time.sleep(2)
        efetua_login(idioma_atual, mostra_tela_titulo, rotina_em_desenvolvimento, bemvindo)

# Função para validar o formato do email
def valida_email(email):
    if "@" not in email:
        return False
    
    partes = email.split("@")
    
    if len(partes) != 2:
        return False
    
    if "." not in partes[1]:
        return False
    
    if not partes[0] or not partes[1].split(".")[0]:
        return False
    
    return True

def cadastro_cliente(idioma_atual, mostra_tela_titulo):
    mostra_tela_titulo()
    # Exibe opções de cadastro de cliente
    print(f"\n{get_mensagem_navegacao(idioma_atual, 'manutencao_cadastro_cliente')}")
    print(f"\n1 - {get_mensagem_navegacao(idioma_atual, 'fazer_cadastro_cliente')}")
    print(f"2 - {get_mensagem_navegacao(idioma_atual, 'consultar_cadastro_cliente')}")
    print(f"3 - {get_mensagem_navegacao(idioma_atual, 'alterar_cadastro_cliente')}")
    print(f"4 - {get_mensagem_navegacao(idioma_atual, 'excluir_cadastro_cliente')}")
    print(f"5 - {get_mensagem_navegacao(idioma_atual, 'voltar')}")

    escolha = input(f"\n{get_mensagem_navegacao(idioma_atual, 'escolha_uma_opcao')}")
    if escolha == '1':
        fazer_cadastro_cliente(idioma_atual, mostra_tela_titulo)
    elif escolha == '2':
        consultar_cadastro_cliente(idioma_atual, mostra_tela_titulo)
        cadastro_cliente(idioma_atual, mostra_tela_titulo)
    elif escolha == '3':
        alterar_cadastro_cliente(idioma_atual, mostra_tela_titulo)
    elif escolha == '4':
        excluir_cadastro(idioma_atual, mostra_tela_titulo)
    elif escolha == '5':
        return
    else:
        print(get_mensagem_navegacao(idioma_atual, 'invalido'))
        time.sleep(2)
        cadastro_cliente(idioma_atual, mostra_tela_titulo)

def fazer_cadastro_cliente(idioma_atual, mostra_tela_titulo):
    mostra_tela_titulo()
    print(f"\n{get_mensagem_navegacao(idioma_atual, 'inclusao_cadastro_cliente')}")

    nome = input(f"\n{get_mensagem_navegacao(idioma_atual, 'Digite_seu_nome')}")
    
    # Loop para obter um email válido
    while True:
        email = input(get_mensagem_navegacao(idioma_atual, 'informe_seu_email'))
        if valida_email(email):
            break
        else:
            print("email não encontrado")
            print(get_mensagem_navegacao(idioma_atual, 'email_invalido'))
    
    # Loop para obter e confirmar a senha
    while True:
        senha = input(get_mensagem_navegacao(idioma_atual, 'informe_senha'))
        confirma_senha = input(get_mensagem_navegacao(idioma_atual, 'informe_senha_novamente'))
        if senha != confirma_senha:
            print(get_mensagem_navegacao(idioma_atual, 'senhas_nao_conferem'))
            time.sleep(2)
            mostra_tela_titulo()
            print(get_mensagem_navegacao(idioma_atual, 'inclusao_cadastro_cliente'))
            print("\nSeu nome: ", nome)
            print("Seu email: ", email)
        elif not valida_senha(senha):
            print(get_mensagem_navegacao(idioma_atual, 'senha_invalida'))
            time.sleep(2)
            mostra_tela_titulo()
            print(get_mensagem_navegacao(idioma_atual, 'inclusao_cadastro_cliente'))
            print("\nSeu nome: ", nome)
            print("Seu email: ", email)
        else:
            break
    
    telefone = input(get_mensagem_navegacao(idioma_atual, 'digite_seu_telefone'))
    
    # Loop para obter a restrição alimentar
    while True:
        restricao_alimentar = input("""Se possuir alguma restrição alimentar, informe: 
    1 - Diabético
    2 - Vegetariano
    3 - Intolerante a Lactose
    4 - Intolerante a Glúten
    5 - Nenhuma
    """)
        if restricao_alimentar in ["1", "2", "3", "4", "5"]:
            break
        else:
            print(get_mensagem_navegacao(idioma_atual, 'opcao_invalida'))
    
    alergia = input("Informe se possui alguma alergia ('Enter' para nenhuma): ")

    # Tenta ler o arquivo para obter o último ID de cliente
    try:
        with open("./txt/clientes.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            if linhas:
                ultimo_id = int(linhas[-1].split(",")[0])
                id_cliente = ultimo_id + 1
            else:
                id_cliente = 1
    except FileNotFoundError:
        id_cliente = 1

    # Dicionário para armazenar os dados do cliente
    cliente = {
        "id": id_cliente,
        "email": email,
        "senha": senha,
        "nome": nome,
        "telefone": telefone,
        "restricao_alimentar": restricao_alimentar,
        "alergia": alergia
    }

    grava_cadastro_cliente(cliente)
    print("\nCadastro efetuado com sucesso!")
    time.sleep(3)

def consultar_cadastro_cliente(idioma_atual, mostra_tela_titulo):
    mostra_tela_titulo()
    print(f"\n{get_mensagem_navegacao(idioma_atual, 'consulta_cadastro_cliente')}")

    # Loop para obter um email válido
    while True:
        email_procurado = input(f"\n{get_mensagem_navegacao(idioma_atual, 'informe_seu_email_cadastrado')}")
        if valida_email(email_procurado):
            break
        else:
            print(f"\n{get_mensagem_navegacao(idioma_atual, 'email_invalido')}")

    restricoes_alimentares = {
        "1": "Diabético",
        "2": "Vegetariano",
        "3": "Intolerante a Lactose",
        "4": "Intolerante a Glúten",
        "5": "Nenhuma"
    }
    
    # Tenta abrir o arquivo e procurar pelo cliente
    try:
        with open("../CARDAPIO.MARCOS/txt/clientes.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            cliente_encontrado = False
            for linha in linhas:
                id_cliente, email, senha, nome, telefone, restricao_alimentar, alergia = linha.strip().split(",")
                if email.lower() == email_procurado.lower():
                    restricao_alimentar_desc = restricoes_alimentares.get(restricao_alimentar, "Nenhuma")
                    alergia = alergia if alergia else "Nenhuma"
                    print(f"\n{get_mensagem_navegacao(idioma_atual, 'nome_cliente')}{nome}")
                    print(f"{get_mensagem_navegacao(idioma_atual, 'email_cliente')}{email}")
                    print(f"{get_mensagem_navegacao(idioma_atual, 'telefone_cliente')}{telefone}")
                    print(f"{get_mensagem_navegacao(idioma_atual, 'restricao_alimentar_cliente')}{restricao_alimentar_desc}")
                    print(f"{get_mensagem_navegacao(idioma_atual, 'alergia_cliente')}{alergia}")
                    cliente_encontrado = True
                    break
            
            if not cliente_encontrado:
                print(get_mensagem_navegacao(idioma_atual, 'cliente_nao_encontrado'))
                
    except FileNotFoundError:
        print(f"\n{get_mensagem_navegacao(idioma_atual, 'arquivo_nao_encontrado')}")

    input(f"\n{get_mensagem_navegacao(idioma_atual, 'aperte_enter_voltar')}")

def alterar_cadastro_cliente(idioma_atual, mostra_tela_titulo):
    mostra_tela_titulo()
    print(f"\n{get_mensagem_navegacao(idioma_atual, 'alteracao_cadastro_cliente')}")
    
    # Loop para obter um email válido
    while True:
        email_procurado = input(f"\n{get_mensagem_navegacao(idioma_atual, 'informe_seu_email_cadastrado')}")
        if valida_email(email_procurado):
            break
        else:
            print(f"\n{get_mensagem_navegacao(idioma_atual, 'email_invalido')}")

    # Loop para obter uma senha válida
    while True:
        senha_procurada = input(get_mensagem_navegacao(idioma_atual, 'informe_senha'))
        if senha_procurada:
            break
        else:
            print(get_mensagem_navegacao(idioma_atual, 'senha_invalida'))

    restricoes_alimentares = {
        "1": get_mensagem_navegacao(idioma_atual, 'diabetico'),
        "2": get_mensagem_navegacao(idioma_atual, 'vegetariano'),
        "3": get_mensagem_navegacao(idioma_atual, 'intolerante_lactose'),
        "4": get_mensagem_navegacao(idioma_atual, 'intolerante_gluten'),
    }

    # Tenta abrir o arquivo de clientes e modificar os dados do cliente encontrado
    try:
        with open("./txt/clientes.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        cliente_encontrado = False
        for i, linha in enumerate(linhas):
            id_cliente, email, senha, nome, telefone, restricao_alimentar, alergia = linha.strip().split(",")
            if email.lower() == email_procurado.lower() and senha == senha_procurada:
                cliente_encontrado = True
                while True:
                    mostra_tela_titulo()
                    print(f"\n1. {get_mensagem_navegacao(idioma_atual, 'nome_cliente')}{nome}")
                    print(f"2. {get_mensagem_navegacao(idioma_atual, 'email_cliente')}{email}")
                    print(f"3. {get_mensagem_navegacao(idioma_atual, 'telefone_cliente')}{telefone}")
                    print(f"4. {get_mensagem_navegacao(idioma_atual, 'restricao_alimentar_cliente')}{restricoes_alimentares.get(restricao_alimentar, get_mensagem_navegacao(idioma_atual, 'nenhuma'))}")
                    print(f"5. {get_mensagem_navegacao(idioma_atual, 'alergia_cliente')}{alergia if alergia else 'Nenhuma'}")
                    escolha = input(f"\n{get_mensagem_navegacao(idioma_atual, 'escolha_alteracao')}")

                    if escolha == '':
                        return

                    if escolha == '1':
                        novo_nome = input(get_mensagem_navegacao(idioma_atual, 'novo_nome'))
                        if novo_nome:
                            nome = novo_nome
                    elif escolha == '3':
                        novo_telefone = input(get_mensagem_navegacao(idioma_atual, 'novo_telefone'))
                        if novo_telefone:
                            telefone = novo_telefone
                    elif escolha == '4':
                        nova_restricao_alimentar = input(get_mensagem_navegacao(idioma_atual, 'nova_restricao_alimentar'))
                        if nova_restricao_alimentar in ["1", "2", "3", "4", "5"]:
                            restricao_alimentar = nova_restricao_alimentar
                        else:
                            print(get_mensagem_navegacao(idioma_atual, 'opcao_invalida'))
                            time.sleep(2)
                            continue
                    elif escolha == '5':
                        nova_alergia = input(get_mensagem_navegacao(idioma_atual, 'nova_alergia'))
                        if nova_alergia:
                            alergia = nova_alergia
                    else:
                        print(get_mensagem_navegacao(idioma_atual, 'opcao_invalida'))
                        time.sleep(2)
                        continue

                    # Atualiza o cadastro do cliente no arquivo
                    linhas[i] = f"{id_cliente},{email},{senha},{nome},{telefone},{restricao_alimentar},{alergia}\n"
                    with open("./txt/clientes.txt", "w") as arquivo:
                        arquivo.writelines(linhas)

                    print(f"\n{get_mensagem_navegacao(idioma_atual, 'cadastro_atualizado')}")
                    time.sleep(2)

        if not cliente_encontrado:
            print(get_mensagem_navegacao(idioma_atual, 'cliente_nao_encontrado'))

    except FileNotFoundError:
        print(get_mensagem_navegacao(idioma_atual, 'arquivo_nao_encontrado'))

    input(get_mensagem_navegacao(idioma_atual, 'aperte_enter_voltar'))

def excluir_cadastro(idioma_atual, mostra_tela_titulo):
    mostra_tela_titulo()
    print(f"\n{get_mensagem_navegacao(idioma_atual, 'exclusao_cadastro_cliente')}")

    # Loop para obter um email válido
    while True:
        email_procurado = input(f"\n{get_mensagem_navegacao(idioma_atual, 'informe_seu_email_cadastrado')}")
        if valida_email(email_procurado):
            break
        else:
            print(f"\n{get_mensagem_navegacao(idioma_atual, 'email_invalido')}")

    # Loop para obter uma senha válida
    while True:
        senha_procurada = input(get_mensagem_navegacao(idioma_atual, 'informe_senha'))
        if senha_procurada:
            break
        else:
            print(f"\n{get_mensagem_navegacao(idioma_atual, 'senha_invalida')}")

    # Tenta abrir o arquivo de clientes e excluir o cadastro do cliente encontrado
    try:
        with open("./txt/clientes.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        cliente_encontrado = False
        for i, linha in enumerate(linhas):
            id_cliente, email, senha, nome, telefone, restricao_alimentar, alergia = linha.strip().split(",")
            if email.lower() == email_procurado.lower() and senha == senha_procurada:
                cliente_encontrado = True
                print(f"\n{get_mensagem_navegacao(idioma_atual, 'cliente_encontrado')} {nome}")
                confirmacao = input(f"\n{get_mensagem_navegacao(idioma_atual, 'confirmacao_exclusao')}")
                if confirmacao.lower() in ["s", "sim", "yes", "y"]:
                    linhas.pop(i)
                    with open("./txt/clientes.txt", "w") as arquivo:
                        arquivo.writelines(linhas)
                    print(get_mensagem_navegacao(idioma_atual, 'cliente_excluido'))
                else:
                    print(get_mensagem_navegacao(idioma_atual, 'exclusao_cliente_cancelada'))
                break

        if not cliente_encontrado:
            print(get_mensagem_navegacao(idioma_atual, 'cliente_nao_encontrado'))

    except FileNotFoundError:
        print(get_mensagem_navegacao(idioma_atual, 'arquivo_nao_encontrado'))

    input(get_mensagem_navegacao(idioma_atual, 'aperte_enter_voltar'))

# Função para validar a força da senha
def valida_senha(senha):
    if len(senha) < 4:
        return False
    if not any(char.isalpha() for char in senha):
        return False
    if not any(char.isdigit() for char in senha):
        return False
    return True

# Função para gravar o cadastro do cliente no arquivo
def grava_cadastro_cliente(cliente):
    with open("./txt/clientes.txt", "a") as arquivo:
        arquivo.write(f"{cliente['id']},{cliente['email']},{cliente['senha']},{cliente['nome']},{cliente['telefone']},{cliente['restricao_alimentar']},{cliente['alergia']}\n")
