# Importa a biblioteca "os" para manipular arquivos e execução de comandos do sistema operacional
import os
import time

from Idioma_navegacao import get_mensagem_navegacao
from Idioma_pratos import get_informacoes_prato

# Define idioma padrão
idioma_atual = 'pt'  

# Cria variavel global codigo_prato
codigo_prato = "000"
cardapio = "000"
logado = False

# Definição global das listas que conterão personaliação de pratos
ingredientes_retirados = []
ingredientes_adicionados = []

# Cria a tela base do programa
def mostra_tela_titulo():
    os.system("cls" if os.name == 'nt' else "clear")  # Limpa a tela, compatível com Windows e Unix
    print('''\033[34m
░█████╗░███████╗░██████╗░█████╗░██████╗░  ██████╗░██╗░██████╗████████╗██████╗░░█████╗░
██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗  ██╔══██╗██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗
██║░░╚═╝█████╗░░╚█████╗░███████║██████╔╝  ██████╦╝██║╚█████╗░░░░██║░░░██████╔╝██║░░██║
██║░░██╗██╔══╝░░░╚═══██╗██╔══██║██╔══██╗  ██╔══██╗██║░╚═══██╗░░░██║░░░██╔══██╗██║░░██║
╚█████╔╝███████╗██████╔╝██║░░██║██║░░██║  ██████╦╝██║██████╔╝░░░██║░░░██║░░██║╚█████╔╝
░╚════╝░╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝  ╚═════╝░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░\033[0m''')

# 1ª Tela - Função para escolher o idioma
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

# 2ª Tela - Função de boas vindas e Login
def bemvindo():
    global logado
    mostra_tela_titulo()
    print(get_mensagem_navegacao(idioma_atual, 'bemvindo'))
    print(get_mensagem_navegacao(idioma_atual, 'mensagem_boas_vindas'))
    print(get_mensagem_navegacao(idioma_atual, "pergunta_fazer_login"))
    print(get_mensagem_navegacao(idioma_atual, "login"))
    print(get_mensagem_navegacao(idioma_atual, "ir_cardapio"))
    print(get_mensagem_navegacao(idioma_atual, "cadastro_de_cliente"))
    print(get_mensagem_navegacao(idioma_atual, "4 - voltar"))

    choice = input(get_mensagem_navegacao(idioma_atual, 'escolha'))
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

# 3ª Tela - Função opcional de efetuar login
def efetua_login():
    mostra_tela_titulo()
    print()
    while True:
        email = input(get_mensagem_navegacao(idioma_atual, 'informe_email'))
        # Exemplo de uso:
        if valida_email(email):
            break
        else:
            print(get_mensagem_navegacao(idioma_atual, 'email_invalido'))

    if email:
        senha = input(get_mensagem_navegacao(idioma_atual, 'informe_senha'))
        if senha:
            if senha == 'admin':
                print(get_mensagem_navegacao(idioma_atual, 'login_sucesso'))
                global logado
                logado = True
                time.sleep(2)
                escolhe_cardapio()
            else:
                print(get_mensagem_navegacao(idioma_atual, 'login_falhou'))
                time.sleep(2)
                efetua_login()

def valida_email(email):
    # Verifica se há um "@" no email
    if "@" not in email:
        return False
    
    # Divide o email em duas partes: antes e depois do "@"
    partes = email.split("@")
    
    # Verifica se restou 2 partes apenas
    if len(partes) != 2:
        return False
    
    # Verifica se há um "." na parte depois do "@"
    if "." not in partes[1]:
        return False
    
    # Verifica se há algo antes do "@" e algo entre o "@" e o "."
    if not partes[0] or not partes[1].split(".")[0]:
        return False
    
    return True

def cadastro_cliente():
    mostra_tela_titulo()
    print(get_mensagem_navegacao(idioma_atual, 'manutencao_cadastro_cliente'))
    print(get_mensagem_navegacao(idioma_atual, 'fazer_cadastro_cliente'))
    print(get_mensagem_navegacao(idioma_atual, 'consultar_cadastro_cliente'))
    print(get_mensagem_navegacao(idioma_atual, 'alterar_cadastro_cliente'))
    print(get_mensagem_navegacao(idioma_atual, 'excluir_cadastro_cliente'))
    print(get_mensagem_navegacao(idioma_atual, '5 - voltar'))

    escolha = input(get_mensagem_navegacao(idioma_atual, 'escolha'))
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
    print(get_mensagem_navegacao(idioma_atual, 'inclusão_cadastro_cliente'))

    nome = input(get_mensagem_navegacao(idioma_atual, 'Digite_seu_nome'))
    while True:
        email = input(get_mensagem_navegacao(idioma_atual, 'informe_email'))
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
            print(get_mensagem_navegacao(idioma_atual, 'inclusão_cadastro_cliente'))
            print("\nSeu nome: ", nome)
            print("Seu email: ", email)
        elif not valida_senha(senha):
            print(get_mensagem_navegacao(idioma_atual, 'senha_invalida'))
            time.sleep(2)
            mostra_tela_titulo()
            print(get_mensagem_navegacao(idioma_atual, 'inclusão_cadastro_cliente'))
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

    # Gerar um ID único para o cliente, baseado no número da linha
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
    print(get_mensagem_navegacao(idioma_atual, 'consulta_cadastro_cliente'))

    while True:
        email_procurado = input(get_mensagem_navegacao(idioma_atual, 'informe_email'))
        if valida_email(email_procurado):
            break
        else:
            print(get_mensagem_navegacao(idioma_atual, 'email_invalido'))

    restricoes_alimentares = {
        "1": "Diabético",
        "2": "Vegetariano",
        "3": "Intolerante a Lactose",
        "4": "Intolerante a Glúten",
        "5": "Nenhuma"
    }
    
    try:
        with open("./txt/clientes.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            cliente_encontrado = False
            for linha in linhas:
                id_cliente, email, senha, nome, telefone, restricao_alimentar, alergia = linha.strip().split(",")
                if email.lower() == email_procurado.lower():
                    restricao_alimentar_desc = restricoes_alimentares.get(restricao_alimentar, "Nenhuma")
                    print(f"{get_mensagem_navegacao(idioma_atual, 'id_cliente')}{id_cliente}")
                    print(f"{get_mensagem_navegacao(idioma_atual, 'nome_cliente')}{nome}")
                    print(f"{get_mensagem_navegacao(idioma_atual, 'email_cliente')}{email}")
                    print(f"{get_mensagem_navegacao(idioma_atual, 'telefone_cliente')}{telefone}")
                    print(f"{get_mensagem_navegacao(idioma_atual, 'restricao_alimentar_cliente')}{restricao_alimentar_desc}")
                    print(f"{get_mensagem_navegacao(idioma_atual, 'alergia_cliente')}{alergia}")
                    cliente_encontrado = True
                    break
            
            if not cliente_encontrado:
                print(get_mensagem_navegacao(idioma_atual, 'cliente_nao_encontrado'))
                
    except FileNotFoundError:
        print(get_mensagem_navegacao(idioma_atual, 'arquivo_nao_encontrado'))

    input(get_mensagem_navegacao(idioma_atual, 'aperte_enter_voltar'))

import time

def alterar_cadastro_cliente():
    mostra_tela_titulo()
    print()
    print(get_mensagem_navegacao(idioma_atual, 'alteracao_cadastro_cliente'))
    print()
    while True:
        email_procurado = input(get_mensagem_navegacao(idioma_atual, 'informe_email'))
        if valida_email(email_procurado):
            break
        else:
            print(get_mensagem_navegacao(idioma_atual, 'email_invalido'))

    restricoes_alimentares = {
        "1": get_mensagem_navegacao(idioma_atual, 'diabetico'),
        "2": get_mensagem_navegacao(idioma_atual, 'vegetariano'),
        "3": get_mensagem_navegacao(idioma_atual, 'intolerante_lactose'),
        "4": get_mensagem_navegacao(idioma_atual, 'intolerante_gluten'),
        "5": get_mensagem_navegacao(idioma_atual, 'nenhuma')
    }

    try:
        with open("./txt/clientes.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        cliente_encontrado = False
        for i, linha in enumerate(linhas):
            id_cliente, email, senha, nome, telefone, restricao_alimentar, alergia = linha.strip().split(",")
            if email.lower() == email_procurado.lower():
                cliente_encontrado = True
                while True:
                    mostra_tela_titulo()
                    print(f"{get_mensagem_navegacao(idioma_atual, 'id_cliente')}{id_cliente}")
                    print(f"1. {get_mensagem_navegacao(idioma_atual, 'nome_cliente')}{nome}")
                    print(f"2. {get_mensagem_navegacao(idioma_atual, 'email_cliente')}{email}")
                    print(f"3. {get_mensagem_navegacao(idioma_atual, 'telefone_cliente')}{telefone}")
                    print(f"4. {get_mensagem_navegacao(idioma_atual, 'restricao_alimentar_cliente')}{restricoes_alimentares.get(restricao_alimentar, get_mensagem_navegacao(idioma_atual, 'nenhuma'))}")
                    print(f"5. {get_mensagem_navegacao(idioma_atual, 'alergia_cliente')}{alergia}")
                    print()
                    escolha = input(get_mensagem_navegacao(idioma_atual, 'escolha_alteracao'))

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

                    print(get_mensagem_navegacao(idioma_atual, 'cadastro_atualizado'))
                    time.sleep(2)

        if not cliente_encontrado:
            print(get_mensagem_navegacao(idioma_atual, 'cliente_nao_encontrado'))

    except FileNotFoundError:
        print(get_mensagem_navegacao(idioma_atual, 'arquivo_nao_encontrado'))

    input(get_mensagem_navegacao(idioma_atual, 'aperte_enter_voltar'))

def excluir_cadastro():
    pass


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

# 4ª Tela - Função para acessar o menu principal
def escolhe_cardapio():
    global cardapio
    mostra_tela_titulo()
    print(get_mensagem_navegacao(idioma_atual, "escolhe_cardapio"))
    print(get_mensagem_navegacao(idioma_atual, "1 - Geral"))
    print(get_mensagem_navegacao(idioma_atual, "2 - Diabetico"))
    print(get_mensagem_navegacao(idioma_atual, "3 - Vegetariano"))
    print(get_mensagem_navegacao(idioma_atual, "4 - Sem Lactose"))
    print(get_mensagem_navegacao(idioma_atual, "5 - Sem Gluten"))
    print(get_mensagem_navegacao(idioma_atual, "6 - Sazonal"))
    if logado:
        print(get_mensagem_navegacao(idioma_atual, "7 - Favoritos"))
        print(get_mensagem_navegacao(idioma_atual, "8 - voltar"))
    else:
        print(get_mensagem_navegacao(idioma_atual, "7 - voltar"))

    try:
        cardapio = int(input(get_mensagem_navegacao(idioma_atual, 'escolha')))
        if (logado == True and cardapio == 8) or (logado == False and cardapio == 7):
            mostra_tela_titulo()
            bemvindo()
        else:
            lista_pratos_cardapio_escolhido(cardapio)

    except ValueError:
        print(get_mensagem_navegacao(idioma_atual, 'DIGITE_NUMERO_VALIDO'))
        time.sleep(2)
        escolhe_cardapio()

# 5ª Tela - Função para escolher o cardápio
def lista_pratos_cardapio_escolhido(cardapio):
    mostra_tela_titulo()
    global codigo_prato

    if cardapio == 1:
        print(get_mensagem_navegacao(idioma_atual, "CARDAPIO_GERAL"))
        ler_arquivo_pratos('./Cardapios/geral.txt')
        print(get_mensagem_navegacao(idioma_atual, "4 - voltar"))
        choice = input(get_mensagem_navegacao(idioma_atual, 'escolha'))
        if choice == '1':
            codigo_prato = '001'
            apresenta_prato_escolhido(codigo_prato)        
        elif choice == '2':
            codigo_prato = '002'
            apresenta_prato_escolhido(codigo_prato)
        elif choice == '3':
            codigo_prato = '003'
            apresenta_prato_escolhido(codigo_prato)
        elif choice == '4':
            escolhe_cardapio()

    elif cardapio == 2:
        print(get_mensagem_navegacao(idioma_atual, "CARDAPIO_DIABETICO"))
        ler_arquivo_pratos('./Cardapios/diabetico.txt')
        print(get_mensagem_navegacao(idioma_atual, "4 - voltar"))
        choice = input(get_mensagem_navegacao(idioma_atual, 'escolha'))
        if choice == '1':
            codigo_prato = '004'
            apresenta_prato_escolhido(codigo_prato)        
        elif choice == '2':
            codigo_prato = '005'
            apresenta_prato_escolhido(codigo_prato)        
        elif choice == '3':
            codigo_prato = '006'
            apresenta_prato_escolhido(codigo_prato)
        elif choice == '4':
            escolhe_cardapio()          
     
    elif cardapio == 3:
        print(get_mensagem_navegacao(idioma_atual, "CARDAPIO_VEGETARIANO"))
        ler_arquivo_pratos('./Cardapios/vegetariano.txt')
        print(get_mensagem_navegacao(idioma_atual, "4 - voltar"))
        choice = input(get_mensagem_navegacao(idioma_atual, 'escolha'))
        if choice == '1':
            codigo_prato = '007'
            apresenta_prato_escolhido(codigo_prato)        
        elif choice == '2':
            codigo_prato = '008'
            apresenta_prato_escolhido(codigo_prato)        
        elif choice == '3':
            codigo_prato = '009'
            apresenta_prato_escolhido(codigo_prato)        
        elif choice == '4':
            escolhe_cardapio()

    elif cardapio == 4:
        print(get_mensagem_navegacao(idioma_atual, "CARDAPIO_SEM_LACTOSE"))
        ler_arquivo_pratos('./Cardapios/sem_lactose.txt')
        print(get_mensagem_navegacao(idioma_atual, "4 - voltar"))
        choice = input(get_mensagem_navegacao(idioma_atual, 'escolha'))
        if choice == '1':
            codigo_prato = '007'
            apresenta_prato_escolhido(codigo_prato)        
        elif choice == '2':
            codigo_prato = '008'
            apresenta_prato_escolhido(codigo_prato)        
        elif choice == '3':
            codigo_prato = '009'
            apresenta_prato_escolhido(codigo_prato)        
        elif choice == '4':
            escolhe_cardapio() 

    elif cardapio == 5:
        print(get_mensagem_navegacao(idioma_atual, "CARDAPIO_SEM_GLUTEN"))
        ler_arquivo_pratos('./Cardapios/sem_gluten.txt')
        print(get_mensagem_navegacao(idioma_atual, "4 - voltar"))
        choice = input(get_mensagem_navegacao(idioma_atual, 'escolha'))
        if choice == '1':
            codigo_prato = '010'
            apresenta_prato_escolhido(codigo_prato)        
        elif choice == '2':
            codigo_prato = '011'
            apresenta_prato_escolhido(codigo_prato)        
        elif choice == '3':
            codigo_prato = '012'
            apresenta_prato_escolhido(codigo_prato)        
        elif choice == '4':
            escolhe_cardapio() 

    elif cardapio == 6:
        print(get_mensagem_navegacao(idioma_atual, "CARDAPIO_SAZONAL"))
        ler_arquivo_pratos('./Cardapios/sazonal.txt')
        print(get_mensagem_navegacao(idioma_atual, "4 - voltar"))
        choice = input(get_mensagem_navegacao(idioma_atual, 'escolha'))
        if choice == '1':
            codigo_prato = '013'
            apresenta_prato_escolhido(codigo_prato)        
        elif choice == '2':
            codigo_prato = '014'
            apresenta_prato_escolhido(codigo_prato)        
        elif choice == '3':
            codigo_prato = '015'
            apresenta_prato_escolhido(codigo_prato)        
        elif choice == '4':
            escolhe_cardapio()

    elif (logado == True and cardapio == 7):
        # print(get_mensagem_navegacao(idioma_atual, "CARDAPIO_FAVORITO"))
        rotina_em_desenvolvimento()
        time.sleep(2)
        escolhe_cardapio()

    elif (logado == False and cardapio == 8):
        escolhe_cardapio()
    else:
        print('\nDigite um Numero Válido')
        time.sleep(2)
        escolhe_cardapio()

def ler_arquivo_pratos(menu_escolhido):
    with open(menu_escolhido, 'r') as arquivo:
        dados = arquivo.readlines()
        for dado in dados:
            print(dado.strip())

# 6ª tela - Lista as opções do menu principal usando dicionario de idiomas
def apresenta_prato_escolhido(codigo_prato):    
    mostra_tela_titulo()
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'prato') + ": " + get_informacoes_prato(codigo_prato, idioma_atual, 'descricao'))
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'lista_ingredientes'))
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'preco_tempo'))

    print(get_mensagem_navegacao(idioma_atual, 'pedir_este_prato'))
    print(get_mensagem_navegacao(idioma_atual, 'nutricional'))
    print(get_mensagem_navegacao(idioma_atual, 'personalize'))
    print(get_mensagem_navegacao(idioma_atual, 'video'))
    print(get_mensagem_navegacao(idioma_atual, '5 - voltar'))
    print(get_mensagem_navegacao(idioma_atual, 'finalizar_pedido'))

    if ingredientes_retirados:
        print(get_mensagem_navegacao(idioma_atual, 'lista_ingredientes_retirados'), ingredientes_retirados)
    if ingredientes_adicionados:
        print(get_mensagem_navegacao(idioma_atual, 'lista_ingredientes_adicionados'), ingredientes_adicionados)
    while True:
        choice = input(get_mensagem_navegacao(idioma_atual, 'escolha'))
        # Escolheu Pedir este Prato
        if choice == '1':
            rotina_em_desenvolvimento()
        # Escolheu opção 2 (Informação Nutricional, Valor calórico e alergênicos)
        if choice == '2':
            mostra_tela_titulo()
            lista_informaçoes_nutricionais()
            mostra_tela_titulo()
            apresenta_prato_escolhido(codigo_prato)
        # Escolheu opção 3 (Personalize seu prato)
        elif choice == '3':
            # mostra_tela_titulo()
            personalizar_prato()
                
        # Escolheu opção 4 (Vídeo de apresentação do prato)
        elif choice == '4':
            print(get_mensagem_navegacao(idioma_atual, 'aguarde'))
            reproduz_video_prato()
            mostra_tela_titulo()
            apresenta_prato_escolhido(codigo_prato)
        # Escolheu opção 5 (voltar)
        elif choice == '5':
            mostra_tela_titulo()
            lista_pratos_cardapio_escolhido(cardapio)
        elif choice == '6':
            finalizar_app()
            break
        else:
            pass

# 7ª tela - Mostra as informações nutricionais do prato
def lista_informaçoes_nutricionais():
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'info_nutricional'))
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'calorias'))
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'carboidratos'))
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'proteinas'))
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'gorduras'))
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'saturadas'))
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'trans'))
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'fibra'))
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'sodio'))
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'base_dieta'))
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'atencao_lactose'))
    input(get_mensagem_navegacao(idioma_atual, 'aperte_enter_voltar'))

def tela_personalizar_prato():
    mostra_tela_titulo()
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'prato'))
    print(get_informacoes_prato(codigo_prato, idioma_atual, 'lista_ingredientes'))
    print(get_mensagem_navegacao(idioma_atual, 'retirar_ingrediente'))
    print(get_mensagem_navegacao(idioma_atual, 'adicionar_ingrediente'))
    print(get_mensagem_navegacao(idioma_atual, '3 - voltar'))

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
        choice = input(get_mensagem_navegacao(idioma_atual, 'escolha'))
        if choice == '1':
            if ingredientes_retirados:
                print(get_mensagem_navegacao(idioma_atual, 'aviso_substituir_ingredientes'))
                ingredientes_retirados = []  # Limpa a lista de ingredientes retirados
            ingrediente = input(get_mensagem_navegacao(idioma_atual, 'digite_ingrediente_retirar'))
            if ingrediente:
                ingredientes_retirados.append(ingrediente)  # Adiciona o novo ingrediente retirado à lista
            else:
                print(get_mensagem_navegacao(idioma_atual, 'sem_ingredientes_retirados'))
        elif choice == '2':
            if ingredientes_adicionados:
                print(get_mensagem_navegacao(idioma_atual, 'aviso_substituir_ingredientes'))
                ingredientes_adicionados = []  # Limpa a lista de ingredientes adicionados
            ingrediente = input(get_mensagem_navegacao(idioma_atual, 'digite_ingrediente_adicionar'))
            if ingrediente:
                ingredientes_adicionados.append(ingrediente)  # Adiciona o novo ingrediente adicionado à lista
            else:
                print(get_mensagem_navegacao(idioma_atual, 'sem_ingredientes_adicionados'))

        elif choice == '3':
            apresenta_prato_escolhido(codigo_prato)
            pass
        else:
            print(get_mensagem_navegacao(idioma_atual, 'invalido'))

# Reproduz o vídeo de apresentação do prato
def reproduz_video_prato():
    # Caminho base onde os vídeos estão armazenados
    base_path = r"C:\Cesar_School\PROJETO\CARDAPIO.MARCOS\Videos"
    # Constrói o caminho completo do arquivo de vídeo
    video_filename = f"{codigo_prato}.mp4"  # Adiciona o código do prato e a extensão .mp4
    path_video = os.path.join(base_path, video_filename)  # Usa os.path.join para construir o caminho completo

    # Verifica se o arquivo de vídeo existe
    if os.path.isfile(path_video):
        # Executa o arquivo de vídeo passando o caminho como argumento
        os.system(f"python PlayMP4Video.py \"{path_video}\"")
    else:
        print("Arquivo de vídeo não encontrado.")

def finalizar_app():
    os.system("cls" if os.name == 'nt' else "clear")  # Limpa a tela, compatível com Windows e Unix
    print("Encerrando o programa...\n", flush=True)
    time.sleep(1)

def rotina_em_desenvolvimento():
    for _ in range(3):  # Faz a frase piscar 2 vezes
        os.system("cls" if os.name == 'nt' else "clear")  # Limpa a tela, compatível com Windows e Unix
        print(get_mensagem_navegacao(idioma_atual, 'rotina_desenvolvimento'), end='', flush=True)
        time.sleep(0.5)  # Tempo com a frase visível
        os.system("cls" if os.name == 'nt' else "clear")  # Limpa a tela
        time.sleep(0.5)  # Tempo com a tela limpa




    


# Função principal
def main():
    mostra_tela_titulo()
    escolher_idioma()
    bemvindo()

# Executa o programa
if __name__ == "__main__":
    main()
