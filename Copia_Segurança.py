import os
import time

from Idioma_navegacao import get_mensagem_navegacao
from Idioma_pratos import get_informacoes_prato

idioma_atual = 'pt'
codigo_prato = "000"
cardapio = "000"
logado = False

ingredientes_retirados = []
ingredientes_adicionados = []

def mostra_tela_titulo():
    os.system("cls" if os.name == 'nt' else "clear")
    print('''\033[34m
░█████╗░███████╗░██████╗░█████╗░██████╗░  ██████╗░██╗░██████╗████████╗██████╗░░█████╗░
██╔══██╗██╔════╝██╔═══╝░██╔══██╗██╔══██╗  ██╔══██╗██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗
██║░░╚═╝█████╗░░╚█████╗░███████║██████╔╝  ██████╦╝██║╚█████╗░░░░██║░░░██████╔╝██║░░██║
██║░░██╗██╔══╝░░░╚═══██╗██╔══██║██╔══██╗  ██╔══██╗██║░╚═══██╗░░░██║░░░██╔══██╗██║░░██║
╚█████╔╝███████╗██████╔╝██║░░██║██║░░██║  ██████╦╝██║██████╔╝░░░██║░░░██║░░██║╚█████╔╝
░╚════╝░╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝  ╚═════╝░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░\033[0m''')

def escolher_idioma():
    global idioma_atual
    print("\nEscolha o idioma / Choose language :")
    print("\n1 - Português (pt)")
    print("2 - Inglês (en)")
    print("3 - Espanhol (es)")
    escolha = input("\nOpção / Option / opción : ")
    if escolha == '1':
        idioma_atual = 'pt'
    elif escolha == '2':
        idioma_atual = 'en'
    else:
        idioma_atual = 'es'

def bemvindo():
    global logado
    mostra_tela_titulo()
    print(f"\n{get_mensagem_navegacao(idioma_atual, 'bemvindo')}")
    print(f"\n{get_mensagem_navegacao(idioma_atual, 'mensagem_boas_vindas')}")
    print(f"\n{get_mensagem_navegacao(idioma_atual, 'pergunta_fazer_login')}")
    print(f"\n1 - {get_mensagem_navegacao(idioma_atual, 'login')}")
    print(f"2 - {get_mensagem_navegacao(idioma_atual, 'ir_cardapio')}")
    print(f"3 - {get_mensagem_navegacao(idioma_atual, 'cadastro_de_cliente')}")
    print(f"4 - {get_mensagem_navegacao(idioma_atual, 'voltar')}")

    choice = input(f"\n{get_mensagem_navegacao(idioma_atual, 'escolha_uma_opcao')}")
    if choice == '1':
        efetua_login()
    elif choice == '2':
        logado = False
        escolhe_cardapio()
    elif choice == '3':
        cadastro_cliente()
        bemvindo()
    elif choice == '4':
        mostra_tela_titulo()
        escolher_idioma()
    else:
        pass

def efetua_login():
    def busca_senha_por_email(email):
        caminho_arquivo = "../CARDAPIO.MARCOS/txt/clientes.txt"
        with open(caminho_arquivo, mode='r', encoding='utf-8') as file:
            for line in file:
                dados = line.strip().split(',')
                if dados[1] == email:
                    return dados[2]
        return None

    mostra_tela_titulo()

    while True:
        email = input(f"\n{get_mensagem_navegacao(idioma_atual, 'informe_seu_email')}")
        
        if email == "":
            bemvindo()
            return
        
        if valida_email(email):
            break
        else:
            print(get_mensagem_navegacao(idioma_atual, 'email_invalido'))

    senha_armazenada = busca_senha_por_email(email)
    if senha_armazenada:
        senha = input(get_mensagem_navegacao(idioma_atual, 'informe_senha'))
        if senha == senha_armazenada:
            print(get_mensagem_navegacao(idioma_atual, 'login_sucesso'))
            global logado
            logado = True
            time.sleep(2)
            escolhe_cardapio()
        else:
            print(get_mensagem_navegacao(idioma_atual, 'login_falhou'))
            time.sleep(2)
            efetua_login()
    else:
        print(get_mensagem_navegacao(idioma_atual, 'email_nao_encontrado'))
        time.sleep(2)
        efetua_login()

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

def cadastro_cliente():
    mostra_tela_titulo()
    print(f"\n{get_mensagem_navegacao(idioma_atual, 'manutencao_cadastro_cliente')}")
    print(f"\n1 - {get_mensagem_navegacao(idioma_atual, 'fazer_cadastro_cliente')}")
    print(f"2 - {get_mensagem_navegacao(idioma_atual, 'consultar_cadastro_cliente')}")
    print(f"3 - {get_mensagem_navegacao(idioma_atual, 'alterar_cadastro_cliente')}")
    print(f"4 - {get_mensagem_navegacao(idioma_atual, 'excluir_cadastro_cliente')}")
    print(f"5 - {get_mensagem_navegacao(idioma_atual, 'voltar')}")

    escolha = input(f"\n{get_mensagem_navegacao(idioma_atual, 'escolha_uma_opcao')}")
    if escolha == '1':
        fazer_cadastro_cliente()
    elif escolha == '2':
        consultar_cadastro_cliente()
        cadastro_cliente()
    elif escolha == '3':
        alterar_cadastro_cliente()
        bemvindo()
    elif escolha == '4':
        excluir_cadastro()
    elif escolha == '5':
        bemvindo()
    else:
        print(get_mensagem_navegacao(idioma_atual, 'invalido'))
        time.sleep(2)
        cadastro_cliente()

def fazer_cadastro_cliente():
    mostra_tela_titulo()
    print(f"\n{get_mensagem_navegacao(idioma_atual, 'inclusao_cadastro_cliente')}")

    nome = input(f"\n{get_mensagem_navegacao(idioma_atual, 'Digite_seu_nome')}")
    while True:
        email = input(get_mensagem_navegacao(idioma_atual, 'informe_seu_email'))
        if valida_email(email):
            break
        else:
            print(get_mensagem_navegacao(idioma_atual, 'email_invalido'))
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

def consultar_cadastro_cliente():
    mostra_tela_titulo()
    print(f"\n{get_mensagem_navegacao(idioma_atual, 'consulta_cadastro_cliente')}")

    while True:
        email_procurado = input(f"\n{get_mensagem_navegacao(idioma_atual, 'informe_seu_email')}")
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

def alterar_cadastro_cliente():
    mostra_tela_titulo()
    print(f"\n{get_mensagem_navegacao(idioma_atual, 'alteracao_cadastro_cliente')}")
    while True:
        email_procurado = input(f"\n{get_mensagem_navegacao(idioma_atual, 'informe_seu_email')}")
        if valida_email(email_procurado):
            break
        else:
            print(f"\n{get_mensagem_navegacao(idioma_atual, 'email_invalido')}")

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

def excluir_cadastro():
    mostra_tela_titulo()
    print(f"\n{get_mensagem_navegacao(idioma_atual, 'exclusao_cadastro_cliente')}")

    while True:
        email_procurado = input(f"\n{get_mensagem_navegacao(idioma_atual, 'informe_seu_email')}")
        if valida_email(email_procurado):
            break
        else:
            print(f"\n{get_mensagem_navegacao(idioma_atual, 'email_invalido')}")

    while True:
        senha_procurada = input(get_mensagem_navegacao(idioma_atual, 'informe_senha'))
        if senha_procurada:
            break
        else:
            print(f"\n{get_mensagem_navegacao(idioma_atual, 'senha_invalida')}")

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

def valida_senha(senha):
    if len(senha) < 4:
        return False
    if not any(char.isalpha() for char in senha):
        return False
    if not any(char.isdigit() for char in senha):
        return False
    return True

def grava_cadastro_cliente(cliente):
    with open("./txt/clientes.txt", "a") as arquivo:
        arquivo.write(f"{cliente['id']},{cliente['email']},{cliente['senha']},{cliente['nome']},{cliente['telefone']},{cliente['restricao_alimentar']},{cliente['alergia']}\n")

def escolhe_cardapio():
    global cardapio
    mostra_tela_titulo()
    print(f"\n{get_mensagem_navegacao(idioma_atual, 'escolhe_cardapio')}")
    print(f"\n1 - {get_mensagem_navegacao(idioma_atual, 'geral')}")
    print(f"2 - {get_mensagem_navegacao(idioma_atual, 'diabetico')}")
    print(f"3 - {get_mensagem_navegacao(idioma_atual, 'vegetariano')}")
    print(f"4 - {get_mensagem_navegacao(idioma_atual, 'sem_Lactose')}")
    print(f"5 - {get_mensagem_navegacao(idioma_atual, 'sem_Gluten')}")
    print(f"6 - {get_mensagem_navegacao(idioma_atual, 'sazonal')}")
    if logado:
        print(f"7 - {get_mensagem_navegacao(idioma_atual, 'favoritos')}")
        print(f"8 - {get_mensagem_navegacao(idioma_atual, 'voltar')}")
    else:
        print(f"7 - {get_mensagem_navegacao(idioma_atual, 'voltar')}")
    try:
        cardapio = int(input(f"\n{get_mensagem_navegacao(idioma_atual, 'escolha_uma_opcao')}"))
        if (logado and cardapio == 8) or (not logado and cardapio == 7):
            mostra_tela_titulo()
            bemvindo()
        else:
            lista_pratos_cardapio_escolhido(cardapio)

    except ValueError:
        print(get_mensagem_navegacao(idioma_atual, 'DIGITE_NUMERO_VALIDO'))
        time.sleep(2)
        escolhe_cardapio()

def lista_pratos_cardapio_escolhido(cardapio):
    mostra_tela_titulo()
    global codigo_prato

    def processar_cardapio(mensagem_cardapio, caminho_arquivo, codigos_pratos):
        print(f"\n{get_mensagem_navegacao(idioma_atual, mensagem_cardapio)}")
        ler_arquivo_pratos(caminho_arquivo)
        choice = input(f"\n{get_mensagem_navegacao(idioma_atual, 'escolha_uma_opcao')}")
        if choice in codigos_pratos:
            codigo_prato = codigos_pratos[choice]
            apresenta_prato_escolhido(codigo_prato)
        elif choice == '4':
            escolhe_cardapio()
        else:
            print(get_mensagem_navegacao(idioma_atual, 'opcao_invalida'))
            time.sleep(2)
            processar_cardapio(mensagem_cardapio, caminho_arquivo, codigos_pratos)

    cardapios = {
        1: ('CARDAPIO_GERAL', './Cardapios/geral.txt', {'1': '001', '2': '002', '3': '003'}),
        2: ('CARDAPIO_DIABETICO', './Cardapios/diabetico.txt', {'1': '004', '2': '005', '3': '006'}),
        3: ('CARDAPIO_VEGETARIANO', './Cardapios/vegetariano.txt', {'1': '007', '2': '008', '3': '009'}),
        4: ('CARDAPIO_SEM_LACTOSE', './Cardapios/sem_lactose.txt', {'1': '010', '2': '011', '3': '012'}),
        5: ('CARDAPIO_SEM_GLUTEN', './Cardapios/sem_gluten.txt', {'1': '013', '2': '014', '3': '015'}),
        6: ('CARDAPIO_SAZONAL', './Cardapios/sazonal.txt', {'1': '016', '2': '017', '3': '018'})
    }

    if cardapio in cardapios:
        mensagem_cardapio, caminho_arquivo, codigos_pratos = cardapios[cardapio]
        processar_cardapio(mensagem_cardapio, caminho_arquivo, codigos_pratos)
    elif logado and cardapio == 7:
        rotina_em_desenvolvimento()
        time.sleep(2)
        escolhe_cardapio()
    elif not logado and cardapio == 8:
        escolhe_cardapio()
    else:
        print('\nDigite um Numero Válido')
        time.sleep(2)
        escolhe_cardapio()

def ler_arquivo_pratos(menu_escolhido):
    with open(menu_escolhido, 'r') as arquivo:
        dados = arquivo.readlines()
        print()
        for dado in dados:
            print(dado.strip())
    print(f"4 - {get_mensagem_navegacao(idioma_atual, 'voltar')}")

def apresenta_prato_escolhido(codigo_prato):
    def finalizar_pedido():
        print(get_mensagem_navegacao(idioma_atual, 'pedido_finalizado'))
        os.system("cls" if os.name == 'nt' else "clear")
        print("Enviando pedido para a cozinha...\n", flush=True)
        time.sleep(2)

    mostra_tela_titulo()
    print(f"\n{get_informacoes_prato(codigo_prato, idioma_atual, 'prato') + ': ' + get_informacoes_prato(codigo_prato, idioma_atual, 'descricao')}")
    print(f"\n{get_informacoes_prato(codigo_prato, idioma_atual, 'lista_ingredientes')}")
    print(f"\n{get_informacoes_prato(codigo_prato, idioma_atual, 'preco_tempo')}")

    print(f"\n1 - {get_mensagem_navegacao(idioma_atual, 'pedir_este_prato')}")
    print(f"2 - {get_mensagem_navegacao(idioma_atual, 'nutricional')}")
    print(f"3 - {get_mensagem_navegacao(idioma_atual, 'personalize')}")
    print(f"4 - {get_mensagem_navegacao(idioma_atual, 'video')}")
    print(f"5 - {get_mensagem_navegacao(idioma_atual, 'voltar')}")
    print(f"6 - {get_mensagem_navegacao(idioma_atual, 'finalizar_pedido')}\n")

    if ingredientes_retirados:
        print(get_mensagem_navegacao(idioma_atual, 'lista_ingredientes_retirados'), ingredientes_retirados)
    if ingredientes_adicionados:
        print(get_mensagem_navegacao(idioma_atual, 'lista_ingredientes_adicionados'), ingredientes_adicionados)
    while True:
        choice = input(f"\n{get_mensagem_navegacao(idioma_atual, 'escolha_uma_opcao')}")
        if choice == '1':
            rotina_em_desenvolvimento()
        if choice == '2':
            mostra_tela_titulo()
            lista_informaçoes_nutricionais()
            mostra_tela_titulo()
            apresenta_prato_escolhido(codigo_prato)
        elif choice == '3':
            mostra_tela_titulo()
            personalizar_prato()
        elif choice == '4':
            print(get_mensagem_navegacao(idioma_atual, 'aguarde'))
            reproduz_video_prato()
            mostra_tela_titulo()
            apresenta_prato_escolhido(codigo_prato)
        elif choice == '5':
            lista_pratos_cardapio_escolhido(cardapio)
        elif choice == '6':
            finalizar_pedido()
            bemvindo()
        else:
            pass

def lista_informaçoes_nutricionais():
    print(f"\n{get_informacoes_prato(codigo_prato, idioma_atual, 'info_nutricional')}")
    print(f"\n{get_informacoes_prato(codigo_prato, idioma_atual, 'calorias')}")
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'carboidratos'))
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'proteinas'))
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'gorduras'))
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'saturadas'))
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'trans'))
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'fibra'))
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'sodio'))
    print(f"\n{get_informacoes_prato(codigo_prato, idioma_atual, 'base_dieta')}")
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'atencao_lactose'))
    input(f"\n{get_mensagem_navegacao(idioma_atual, 'aperte_enter_voltar')}")

def tela_personalizar_prato():
    print(f"\n{get_informacoes_prato(codigo_prato, idioma_atual, 'prato')}")
    print(f"\n{get_informacoes_prato(codigo_prato, idioma_atual, 'lista_ingredientes')}")
    print(f"\n1 - {get_mensagem_navegacao(idioma_atual, 'retirar_ingrediente')}")
    print(f"2 - {get_mensagem_navegacao(idioma_atual, 'adicionar_ingrediente')}")
    print(f"3 - {get_mensagem_navegacao(idioma_atual, 'voltar')}")

def personalizar_prato():
    choice = '0'
    global ingredientes_retirados 
    global ingredientes_adicionados

    tela_personalizar_prato()
    
    if ingredientes_retirados:
        print(get_mensagem_navegacao(idioma_atual, 'lista_ingredientes_retirados'), ingredientes_retirados)
    if ingredientes_adicionados:
        print(get_mensagem_navegacao(idioma_atual, 'lista_ingredientes_adicionados'), ingredientes_adicionados)

    while choice.isdigit and choice != '3':
        choice = input(f"\n{get_mensagem_navegacao(idioma_atual, 'escolha_uma_opcao')}")
        if choice == '1':
            if ingredientes_retirados:
                print(get_mensagem_navegacao(idioma_atual, 'aviso_substituir_ingredientes'))
                ingredientes_retirados = []
            ingrediente = input(get_mensagem_navegacao(idioma_atual, 'digite_ingrediente_retirar'))
            if ingrediente:
                ingredientes_retirados.append(ingrediente)
            else:
                print(get_mensagem_navegacao(idioma_atual, 'sem_ingredientes_retirados'))
        elif choice == '2':
            if ingredientes_adicionados:
                print(get_mensagem_navegacao(idioma_atual, 'aviso_substituir_ingredientes'))
                ingredientes_adicionados = []
            ingrediente = input(get_mensagem_navegacao(idioma_atual, 'digite_ingrediente_adicionar'))
            if ingrediente:
                ingredientes_adicionados.append(ingrediente)
            else:
                print(get_mensagem_navegacao(idioma_atual, 'sem_ingredientes_adicionados'))

        elif choice == '3':
            apresenta_prato_escolhido(codigo_prato)
            pass
        else:
            print(get_mensagem_navegacao(idioma_atual, 'invalido'))

def reproduz_video_prato():
    base_path = r"C:\Cesar_School\PROJETO\CARDAPIO.MARCOS\Videos"
    video_filename = "007.mp4"
    path_video = os.path.join(base_path, video_filename)

    if os.path.isfile(path_video):
        os.system(f"python PlayMP4Video.py \"{path_video}\"")
    else:
        print("Arquivo de vídeo não encontrado.")

def finalizar_app():
    os.system("cls" if os.name == 'nt' else "clear")
    print("Encerrando aplicação...\n", flush=True)
    time.sleep(2)

def rotina_em_desenvolvimento():
    for _ in range(3):
        os.system("cls" if os.name == 'nt' else "clear")
        print(get_mensagem_navegacao(idioma_atual, 'rotina_desenvolvimento'), end='', flush=True)
        time.sleep(0.5)
        os.system("cls" if os.name == 'nt' else "clear")
        time.sleep(0.5)

def main():
    mostra_tela_titulo()
    escolher_idioma()
    bemvindo()

if __name__ == "__main__":
    main()
