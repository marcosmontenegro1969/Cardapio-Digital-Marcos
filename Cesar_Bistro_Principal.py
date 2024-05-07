# Importa a biblioteca "os" para manipular arquivos e execução de comandos do sistema operacional
import os
import time

# import curses
from Idiomas import get_mensagem

# Idioma padrão
idioma_atual = 'pt'  

# Definição global da variável ingredientes_personalizados
ingredientes_retirados = []
ingredientes_adicionados = []

# Cria a tela base do programa
def tela_titulo():
    os.system("cls" if os.name == 'nt' else "clear")  # Limpa a tela, compatível com Windows e Unix
    print('''\033[34m
░█████╗░███████╗░██████╗░█████╗░██████╗░  ██████╗░██╗░██████╗████████╗██████╗░░█████╗░
██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗  ██╔══██╗██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗
██║░░╚═╝█████╗░░╚█████╗░███████║██████╔╝  ██████╦╝██║╚█████╗░░░░██║░░░██████╔╝██║░░██║
██║░░██╗██╔══╝░░░╚═══██╗██╔══██║██╔══██╗  ██╔══██╗██║░╚═══██╗░░░██║░░░██╔══██╗██║░░██║
╚█████╔╝███████╗██████╔╝██║░░██║██║░░██║  ██████╦╝██║██████╔╝░░░██║░░░██║░░██║╚█████╔╝
░╚════╝░╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝  ╚═════╝░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░\033[0m''')

# Função para escolher o idioma
def escolher_idioma():
    global idioma_atual
    print("\nEscolha o idioma / Choose language :")
    print("1 - Português")
    print("2 - Inglês")
    escolha = input("\nOpção / Option: ")
    if escolha == '1':
        idioma_atual = 'pt'
    else:
        idioma_atual = 'en'

# Lista as opções do menu principal usando dicionario de idiomas
def lista_pedido_prato():    
    print(get_mensagem(idioma_atual, 'Prato') + ": " + get_mensagem(idioma_atual, 'descrição'))
    print(get_mensagem(idioma_atual, 'lista_ingredientes'))
    print(get_mensagem(idioma_atual, 'preco_tempo'))

    print(get_mensagem(idioma_atual, 'pedir_este_prato'))
    print(get_mensagem(idioma_atual, 'nutricional'))
    print(get_mensagem(idioma_atual, 'personalize'))
    print(get_mensagem(idioma_atual, 'video'))
    print(get_mensagem(idioma_atual, '5 voltar'))
    print(get_mensagem(idioma_atual, 'finalizar_pedido'))

    if ingredientes_retirados:
        print("Ingredientes retirados:", ingredientes_retirados)
    if ingredientes_adicionados:
        print("Ingredientes adicionados:", ingredientes_adicionados)

def lista_informaçoes_nutricionais():
    print(get_mensagem(idioma_atual, 'info_nutricional'))
    print(get_mensagem(idioma_atual, 'calorias'))
    print(get_mensagem(idioma_atual, 'carboidratos'))
    print(get_mensagem(idioma_atual, 'proteinas'))
    print(get_mensagem(idioma_atual, 'gorduras'))
    print(get_mensagem(idioma_atual, 'saturadas'))
    print(get_mensagem(idioma_atual, 'trans'))
    print(get_mensagem(idioma_atual, 'fibra'))
    print(get_mensagem(idioma_atual, 'sodio'))
    print(get_mensagem(idioma_atual, 'base_dieta'))
    print(get_mensagem(idioma_atual, 'atencao_lactose'))
    input(get_mensagem(idioma_atual, 'aperte_enter'))

def tela_personalizar_prato():
    print(get_mensagem(idioma_atual, 'Prato'))
    print(get_mensagem(idioma_atual, 'lista_ingredientes'))
    print(get_mensagem(idioma_atual, 'retirar_ingrediente'))
    print(get_mensagem(idioma_atual, 'adicionar_ingrediente'))
    print(get_mensagem(idioma_atual, '3 voltar'))


def personalizar_prato():
    choice = '0'
    global ingredientes_retirados 
    global ingredientes_adicionados

    tela_personalizar_prato()
    
    if ingredientes_retirados:
        print(get_mensagem(idioma_atual, 'lista_ingredientes_retirados'), ingredientes_retirados)
    if ingredientes_adicionados:
        print(get_mensagem(idioma_atual, 'lista_ingredientes_adicionados'), ingredientes_adicionados)

    while choice.isdigit and choice != '3':
        choice = input(get_mensagem(idioma_atual, 'escolha'))
        if choice == '1':
            if ingredientes_retirados:
                print(get_mensagem(idioma_atual, 'aviso_substituir_ingredientes'))
                ingredientes_retirados = []  # Limpa a lista de ingredientes retirados
            ingrediente = input(get_mensagem(idioma_atual, 'ingredientes_retirados'))
            if ingrediente:
                ingredientes_retirados.append(ingrediente)  # Adiciona o novo ingrediente retirado à lista
            else:
                print(get_mensagem(idioma_atual, 'sem_ingredientes_retirados'))
        elif choice == '2':
            if ingredientes_adicionados:
                print(get_mensagem(idioma_atual, 'aviso_substituir_ingredientes'))
                ingredientes_adicionados = []  # Limpa a lista de ingredientes adicionados
            ingrediente = input(get_mensagem(idioma_atual, 'ingredientes_adicionados'))
            if ingrediente:
                ingredientes_adicionados.append(ingrediente)  # Adiciona o novo ingrediente adicionado à lista
            else:
                print(get_mensagem(idioma_atual, 'sem_ingredientes_adicionados'))

        elif choice == '3':
            tela_titulo()
            lista_pedido_prato()
            break
        else:
            print(get_mensagem(idioma_atual, 'invalido'))

# Reproduz o vídeo de apresentação do prato
def reproduz_video_prato():
    # Verifica se o arquivo de vídeo existe
    if os.path.isfile("Strogonoff.mp4"):
        # Executa o arquivo de vídeo
        os.system("python PlayMP4Video.py")
    else:
        print("Arquivo de vídeo não encontrado.")

def finalizar_app():
    os.system("cls" if os.name == 'nt' else "clear")  # Limpa a tela, compatível com Windows e Unix
    print("Encerrando o programa...\n", flush=True)
    time.sleep(1)

def rotina_em_desenvolvimento():
    for _ in range(3):  # Faz a frase piscar 2 vezes
        os.system("cls" if os.name == 'nt' else "clear")  # Limpa a tela, compatível com Windows e Unix
        print("ESTA ROTINA ESTÁ EM DESENVOLVIMENTO...\n", flush=True)
        time.sleep(0.5)  # Tempo com a frase visível
        os.system("cls" if os.name == 'nt' else "clear")  # Limpa a tela
        time.sleep(0.5)  # Tempo com a tela limpa

    tela_titulo()
    lista_pedido_prato()
 
# Função principal
def main():
    tela_titulo()
    escolher_idioma()
    tela_titulo()
    lista_pedido_prato()
    while True:
        choice = input(get_mensagem(idioma_atual, 'escolha'))
        # Escolheu Pedir este Prato
        if choice == '1':
            rotina_em_desenvolvimento()
        # Escolheu opção 2 (Informação Nutricional, Valor calórico e alergênicos)
        if choice == '2':
            tela_titulo()
            lista_informaçoes_nutricionais()
            tela_titulo()
            lista_pedido_prato()
        # Escolheu opção 3 (Personalize seu prato)
        elif choice == '3':
            tela_titulo()
            personalizar_prato()
                
        # Escolheu opção 4 (Vídeo de apresentação do prato)
        elif choice == '4':
            print(get_mensagem(idioma_atual, 'aguarde'))
            reproduz_video_prato()
            tela_titulo()
            lista_pedido_prato()
        # Escolheu opção 5 (voltar)
        elif choice == '5':
            pass
        elif choice == '6':
            # print(get_mensagem(idioma_atual, 'saida'))
            finalizar_app()
            break
        else:
            pass
            # print (choice)
            # print(get_mensagem(idioma_atual, 'invalido'))

# Executa o programa
if __name__ == "__main__":
    main()
