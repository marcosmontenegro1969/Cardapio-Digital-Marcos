import os
import time
from Idioma_navegacao import get_mensagem_navegacao  # Função para obter mensagens de navegação em diferentes idiomas
from Idioma_pratos import get_informacoes_prato  # Função para obter informações sobre os pratos

# Variáveis globais
logado = False
ingredientes_retirados = []
ingredientes_adicionados = []

# Função para exibir o menu de escolha de cardápio
def escolhe_cardapio(idioma_atual, mostra_tela_titulo, rotina_em_desenvolvimento, bemvindo):
    global logado
    mostra_tela_titulo()
    # Exibe as opções de cardápio
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

    # Captura e processa a escolha do cardápio
    try:
        cardapio = int(input(f"\n{get_mensagem_navegacao(idioma_atual, 'escolha_uma_opcao')}"))
        if (logado and cardapio == 8) or (not logado and cardapio == 7):
            bemvindo(idioma_atual)
        else:
            lista_pratos_cardapio_escolhido(idioma_atual, cardapio, mostra_tela_titulo, rotina_em_desenvolvimento, bemvindo)
    except ValueError:
        print(get_mensagem_navegacao(idioma_atual, 'DIGITE_NUMERO_VALIDO'))
        time.sleep(2)
        escolhe_cardapio(idioma_atual, mostra_tela_titulo, rotina_em_desenvolvimento, bemvindo)

# Função para listar os pratos do cardápio escolhido
def lista_pratos_cardapio_escolhido(idioma_atual, cardapio, mostra_tela_titulo, rotina_em_desenvolvimento, bemvindo):
    global logado
    global ingredientes_retirados
    global ingredientes_adicionados
    mostra_tela_titulo()

    # Função auxiliar para processar o cardápio
    def processar_cardapio(mensagem_cardapio, caminho_arquivo, codigos_pratos):
        print(f"\n{get_mensagem_navegacao(idioma_atual, mensagem_cardapio)}")
        ler_arquivo_pratos(caminho_arquivo, idioma_atual)
        choice = input(f"\n{get_mensagem_navegacao(idioma_atual, 'escolha_uma_opcao')}")
        if choice in codigos_pratos:
            codigo_prato = codigos_pratos[choice]
            apresenta_prato_escolhido(idioma_atual, codigo_prato, mostra_tela_titulo, cardapio, rotina_em_desenvolvimento, bemvindo)
        elif choice == '4':
            escolhe_cardapio(idioma_atual, mostra_tela_titulo, rotina_em_desenvolvimento, bemvindo)      
        elif choice == '5':
            finalizar_pedido(idioma_atual)
            escolhe_cardapio(idioma_atual, mostra_tela_titulo, rotina_em_desenvolvimento, bemvindo)
        else:
            print(get_mensagem_navegacao(idioma_atual, 'opcao_invalida'))
            time.sleep(2)
            processar_cardapio(mensagem_cardapio, caminho_arquivo, codigos_pratos)

    # Mapeamento dos cardápios para seus respectivos arquivos e códigos de pratos
    cardapios = {
        1: ('CARDAPIO_GERAL', './Cardapios/geral.txt', {'1': '001', '2': '002', '3': '003'}),
        2: ('CARDAPIO_DIABETICO', './Cardapios/diabetico.txt', {'1': '004', '2': '005', '3': '006'}),
        3: ('CARDAPIO_VEGETARIANO', './Cardapios/vegetariano.txt', {'1': '007', '2': '008', '3': '009'}),
        4: ('CARDAPIO_SEM_LACTOSE', './Cardapios/sem_lactose.txt', {'1': '010', '2': '011', '3': '012'}),
        5: ('CARDAPIO_SEM_GLUTEN', './Cardapios/sem_gluten.txt', {'1': '013', '2': '014', '3': '015'}),
        6: ('CARDAPIO_SAZONAL', './Cardapios/sazonal.txt', {'1': '016', '2': '017', '3': '018'})
    }

    # Processa o cardápio selecionado
    if cardapio in cardapios:
        mensagem_cardapio, caminho_arquivo, codigos_pratos = cardapios[cardapio]
        processar_cardapio(mensagem_cardapio, caminho_arquivo, codigos_pratos)
    elif logado and cardapio == 7:
        rotina_em_desenvolvimento(idioma_atual)
        time.sleep(2)
        escolhe_cardapio(idioma_atual, mostra_tela_titulo, rotina_em_desenvolvimento, bemvindo)
    elif not logado and cardapio == 8:
        escolhe_cardapio(idioma_atual, mostra_tela_titulo, rotina_em_desenvolvimento, bemvindo)
    else:
        print('\nDigite um Numero Válido')
        time.sleep(2)
        escolhe_cardapio(idioma_atual, mostra_tela_titulo, rotina_em_desenvolvimento, bemvindo)

# Função para ler o arquivo de pratos e exibir o conteúdo
def ler_arquivo_pratos(menu_escolhido, idioma_atual):
    with open(menu_escolhido, 'r') as arquivo:
        dados = arquivo.readlines()
        print()
        for dado in dados:
            print(dado.strip())
    print(f"4 - {get_mensagem_navegacao(idioma_atual, 'voltar')}")
    print(f"5 - {get_mensagem_navegacao(idioma_atual, 'finalizar_pedido')}")

# Função para apresentar o prato escolhido
def apresenta_prato_escolhido(idioma_atual, codigo_prato, mostra_tela_titulo, cardapio, rotina_em_desenvolvimento, bemvindo):
    mostra_tela_titulo()
    # Exibe as informações detalhadas do prato
    print(f"\n{get_informacoes_prato(codigo_prato, idioma_atual, 'prato') + ': ' + get_informacoes_prato(codigo_prato, idioma_atual, 'descricao')}")
    print(f"\n{get_informacoes_prato(codigo_prato, idioma_atual, 'lista_ingredientes')}")
    print(f"\n{get_informacoes_prato(codigo_prato, idioma_atual, 'preco_tempo')}")

    # Exibe as opções para o prato escolhido
    print(f"\n1 - {get_mensagem_navegacao(idioma_atual, 'pedir_este_prato')}")
    print(f"2 - {get_mensagem_navegacao(idioma_atual, 'nutricional')}")
    print(f"3 - {get_mensagem_navegacao(idioma_atual, 'personalize')}")
    print(f"4 - {get_mensagem_navegacao(idioma_atual, 'video')}")
    print(f"5 - {get_mensagem_navegacao(idioma_atual, 'voltar')}")
    print(f"6 - {get_mensagem_navegacao(idioma_atual, 'finalizar_pedido')}")

    # Exibe os ingredientes retirados e adicionados, se houver
    if ingredientes_retirados:
        print(get_mensagem_navegacao(idioma_atual, 'lista_ingredientes_retirados'), ingredientes_retirados)
    if ingredientes_adicionados:
        print(get_mensagem_navegacao(idioma_atual, 'lista_ingredientes_adicionados'), ingredientes_adicionados)

    # Processa a escolha do usuário para o prato selecionado
    while True:
        choice = input(f"\n{get_mensagem_navegacao(idioma_atual, 'escolha_uma_opcao')}")
        if choice == '1':
            rotina_em_desenvolvimento(idioma_atual)
            lista_pratos_cardapio_escolhido(idioma_atual, cardapio, mostra_tela_titulo, rotina_em_desenvolvimento, bemvindo)
        elif choice == '2':
            lista_informacoes_nutricionais(idioma_atual, codigo_prato)
            apresenta_prato_escolhido(idioma_atual, codigo_prato, mostra_tela_titulo, cardapio, rotina_em_desenvolvimento, bemvindo)
        elif choice == '3':
            personalizar_prato(idioma_atual, codigo_prato, mostra_tela_titulo, cardapio, rotina_em_desenvolvimento, bemvindo)
        elif choice == '4':
            print(get_mensagem_navegacao(idioma_atual, 'aguarde'))
            reproduz_video_prato()
            apresenta_prato_escolhido(idioma_atual, codigo_prato, mostra_tela_titulo, cardapio, rotina_em_desenvolvimento, bemvindo)
        elif choice == '5':
            lista_pratos_cardapio_escolhido(idioma_atual, cardapio, mostra_tela_titulo, rotina_em_desenvolvimento, bemvindo)
        elif choice == '6':
            finalizar_pedido(idioma_atual)
            escolhe_cardapio(idioma_atual, mostra_tela_titulo, rotina_em_desenvolvimento, bemvindo)
        else:
            pass

# Função para listar as informações nutricionais do prato
def lista_informacoes_nutricionais(idioma_atual, codigo_prato):
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

# Função para exibir a tela de personalização do prato
def tela_personalizar_prato(idioma_atual, codigo_prato):
    print(f"\n{get_informacoes_prato(codigo_prato, idioma_atual, 'prato')}")
    print(f"\n{get_informacoes_prato(codigo_prato, idioma_atual, 'lista_ingredientes')}")
    print(f"\n1 - {get_mensagem_navegacao(idioma_atual, 'retirar_ingrediente')}")
    print(f"2 - {get_mensagem_navegacao(idioma_atual, 'adicionar_ingrediente')}")
    print(f"3 - {get_mensagem_navegacao(idioma_atual, 'voltar')}")

# Função para personalizar o prato
def personalizar_prato(idioma_atual, codigo_prato, mostra_tela_titulo, cardapio, rotina_em_desenvolvimento, bemvindo):
    choice = '0'
    global ingredientes_retirados 
    global ingredientes_adicionados

    tela_personalizar_prato(idioma_atual, codigo_prato)
    
    if ingredientes_retirados:
        print(get_mensagem_navegacao(idioma_atual, 'lista_ingredientes_retirados'), ingredientes_retirados)
    if ingredientes_adicionados:
        print(get_mensagem_navegacao(idioma_atual, 'lista_ingredientes_adicionados'), ingredientes_adicionados)

    # Processa a escolha do usuário para personalizar o prato
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
            apresenta_prato_escolhido(idioma_atual, codigo_prato, mostra_tela_titulo, cardapio, rotina_em_desenvolvimento, bemvindo)
            pass
        else:
            print(get_mensagem_navegacao(idioma_atual, 'invalido'))

# Função para reproduzir vídeo do prato
def reproduz_video_prato():
    base_path = r"C:\Cesar_School\PROJETO\CARDAPIO.MARCOS\Videos"
    video_filename = "007.mp4"
    path_video = os.path.join(base_path, video_filename)

    if os.path.isfile(path_video):
        os.system(f"python PlayMP4Video.py \"{path_video}\"")
    else:
        print("Arquivo de vídeo não encontrado.")

# Função para finalizar o pedido
def finalizar_pedido(idioma_atual):
    print(get_mensagem_navegacao(idioma_atual, 'pedido_finalizado'))
    os.system("cls" if os.name == 'nt' else "clear")
    print("Enviando pedido para a cozinha...\n", flush=True)
    time.sleep(2)
