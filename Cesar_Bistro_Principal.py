import os
import time
from clientes import efetua_login, cadastro_cliente
from pratos import escolhe_cardapio
from Idioma_navegacao import get_mensagem_navegacao

logado = False
idioma_atual = 'pt'  # Valor inicial padrão para o idioma

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
    while True:
        print("\nEscolha o idioma / Choose language / Elige lengua / Scegli la lingua/ Sprache wählen:")
        print("\n1 - Português (pt)")
        print("2 - Inglês (en)")
        print("3 - Espanhol (es)")
        print("4 - Italiano (it)")
        print("5 - Alemão (de)")
        escolha = input("\nOpção / Option / opción / opzione / Möglichkeit : ")
        if escolha == '1':
            return 'pt'
        elif escolha == '2':
            return 'en'
        elif escolha == '3':
            return 'es'
        elif escolha == '4':
            return 'it'
        elif escolha == '5':
            return 'de'
        else:
            # print("\nOpção inválida! Tente novamente.")

            mostra_tela_titulo()


def bemvindo(idioma_atual):
    global logado
    while True:
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
            try:
                efetua_login(idioma_atual, mostra_tela_titulo, rotina_em_desenvolvimento, bemvindo)
            except Exception as e:
                print(f"\nErro ao efetuar login: {e}")
            bemvindo(idioma_atual)
        elif choice == '2':
            logado = False
            try:
                escolhe_cardapio(idioma_atual, mostra_tela_titulo, rotina_em_desenvolvimento, bemvindo)
            except Exception as e:
                print(f"\nErro ao escolher cardápio: {e}")
        elif choice == '3':
            try:
                cadastro_cliente(idioma_atual, mostra_tela_titulo)
            except Exception as e:
                print(f"\nErro ao cadastrar cliente: {e}")
            bemvindo(idioma_atual)
        elif choice == '4' or choice == '':
            mostra_tela_titulo()
            idioma_atual = escolher_idioma()
            bemvindo(idioma_atual)
        else:
            escolha_invalida()
            bemvindo(idioma_atual)

def escolha_invalida():
    for _ in range(3):
        os.system("cls" if os.name == 'nt' else "clear")
        print(get_mensagem_navegacao(idioma_atual, 'opcao_invalida'), end='', flush=True)
        time.sleep(0.5)
        os.system("cls" if os.name == 'nt' else "clear")
        time.sleep(0.5)
            


# def finalizar_app():
#     os.system("cls" if os.name == 'nt' else "clear")
#     print("Encerrando aplicação...\n", flush=True)
#     time.sleep(2)

def rotina_em_desenvolvimento(idioma_atual):
    for _ in range(3):
        os.system("cls" if os.name == 'nt' else "clear")
        print(get_mensagem_navegacao(idioma_atual, 'rotina_desenvolvimento'), end='', flush=True)
        time.sleep(0.5)
        os.system("cls" if os.name == 'nt' else "clear")
        time.sleep(0.5)

def main():
    mostra_tela_titulo()
    idioma_atual = escolher_idioma()
    bemvindo(idioma_atual)

if __name__ == "__main__":
    main()
