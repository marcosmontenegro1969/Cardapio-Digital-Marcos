# Mensagens em português e inglês
mensagens = {
    'pt': {
        'pedir_este_prato': "\n1 - PEDIR ESTE PRATO.",
        'nutricional': "2 - Informação Nutricional, Valor calórico e alergênicos",
        'personalize': "3 - Personalize seu prato",
        'digite_ingrediente_retirar': "Digite o ingrediente a ser RETIRADO: ",
        'digite_ingrediente_adicionar': "Digite o ingrediente a ser ADICIONADO: ",
        'sem_ingredientes_retirados': "Nenhum ingrediente será retirado.",
        'sem_ingredientes_adicionados': "Nenhum ingrediente será adicionado.",
        'lista_ingredientes_retirados': "Ingredientes a serem RETIRADOS: ",
        'lista_ingredientes_adicionados': "Ingredientes a serem ADICIONADOS: ",
        'aviso_substituir_ingredientes': "\nOs ingredientes que você já informou serão substituídos por estes.",
        'video': "4 - Vídeo de apresentação do prato",
        'video_nao_encontrado': "Arquivo de vídeo não encontrado.",
        '3 voltar': "3 - Voltar",
        '4 voltar': "4 - Voltar",
        '5 voltar': "5 - Voltar",
        'finalizar_pedido': "6 - finalizar pedido",
        'escolha': "\nEscolha uma opção: ",
        'retirar_ingrediente': "\n1 - Retirar ingrediente",
        'adicionar_ingrediente': "2 - Adicionar ingrediente",
        'aperte_enter': "\nAperte Enter para voltar a tela inicial ",
        'saida': "Saindo do programa.",
        'invalido': "Opção inválida, tente novamente.",
        'rotina_desenvolvimento': 'Rotina em desenvolvimento...',
        'aguarde': "Aguarde..."
    },
    'en': {
        'pedir_este_prato': "\n1 - ORDER THIS DISH.",
        'nutricional': "2 - Nutritional Information, Caloric Value, and Allergens",
        'personalize': "3 - Personalize your dish",
        'digite_ingrediente_retirar': "Enter the ingredient to be REMOVED: ",
        'digite_ingrediente_adicionar': "Enter the ingredient to be ADDED: ",
        'sem_ingredientes_retirados': "No ingredients will be removed.",
        'sem_ingredientes_adicionados': "No ingredients will be added.",
        'lista_ingredientes_retirados': "Ingredients to be REMOVED: ",
        'lista_ingredientes_adicionados': "Ingredients to be ADDED: ",
        'aviso_substituir_ingredientes': "\nThe ingredients you have already entered will be replaced by these.",
        'video': "4 - Dish presentation video",
        'video_nao_encontrado': "Video file not found.",
        '3 voltar': "3 - Go back",
        '4 voltar': "4 - Go back",
        '5 voltar': "5 - Go back",
        'finalizar_pedido': "6 - finalize order",
        'escolha': "\nChoose an option: ",
        'retirar_ingrediente': "\n1 - Remove ingredient",
        'adicionar_ingrediente': "2 - Add ingredient",
        'aperte_enter': "\nPress Enter to return to the main screen ",
        'saida': "Exiting the program.",
        'invalido': "Invalid option, try again.",
        'rotina_desenvolvimento': 'Development routine...',
        'aguarde': "Please wait..."
    }
}

def get_mensagem_navegacao(idioma, chave):
    """Returns the message for the specified language and key."""
    return mensagens[idioma].get(chave, "Message not found")
