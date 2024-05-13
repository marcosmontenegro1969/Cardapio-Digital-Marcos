# Mensagens em português e inglês
cardapio = {
    '001': {
        'pt': {
            'prato': "\nSTROGONOFF VEGETARIANO",
            'descrição': "Pedaços suculentos de cogumelos frescos e proteína de soja texturizada, delicadamente cozidos em um molho cremoso e rico, repleto de temperos aromáticos. Servido com arroz soltinho e batatas douradas, este prato é uma celebração da culinária vegetariana, perfeito para saciar seus desejos sem abrir mão do sabor e da tradição.",
            'lista_ingredientes': "\nIngredientes: Frango, sal, pimenta, azeite, cebola, beringela, tomate, salsa, creme de leite, ketchup, mostarda",
            'preco_tempo': "\nPreço: R$ 45,00 - Tempo estimado de preparo: 20 minutos",
            'info_nutricional': "\nInformação Nutricional (Porção de 60g):",
            'calorias': "\nValor Calórico: 114,6kcal (5,3% VD)",
            'carboidratos': "Carboidratos: 2,77g (1% VD)",
            'proteinas': "Proteínas: 7,6g (9,3% VD)",
            'gorduras': "Gorduras totais: 7,8g (15,6% VD)",
            'saturadas': "Gorduras saturadas: 0g",
            'trans': "Gorduras trans: 0g",
            'fibra': "Fibra alimentar: 2,9g (8,8% VD)",
            'sodio': "Sódio: 114mg (6% VD)",
            'base_dieta': "*Valores diários com base em dieta de 2.000kcal ou 8.400kj.",
            'atencao_lactose': "Atenção : Este alimento CONTÉM LACTOSE",
        },
        'en': {
            'prato': "\nVEGETARIAN STROGANOFF",
            'descrição': "Juicy chunks of fresh mushrooms and textured soy protein, delicately cooked in a creamy and rich sauce full of aromatic spices. Served with fluffy rice and golden potatoes, this dish is a celebration of vegetarian cuisine, perfect for satisfying your cravings without sacrificing flavor and tradition.",
            'lista_ingredientes': "\nIngredients: Chicken, salt, pepper, olive oil, onion, eggplant, tomato, parsley, cream, ketchup, mustard",
            'preco_tempo': "\nPrice: $ 45.00 - Estimated preparation time: 20 minutes",
            'info_nutricional': "\nNutritional Information (Serving of 60g):",
            'calorias': "\nCaloric Value: 114.6 kcal (5.3% DV)",
            'carboidratos': "Carbohydrates: 2.77g (1% DV)",
            'proteinas': "Proteins: 7.6g (9.3% DV)",
            'gorduras': "Total Fats: 7.8g (15.6% DV)",
            'saturadas': "Saturated Fats: 0g",
            'trans': "Trans Fats: 0g",
            'fibra': "Dietary Fiber: 2.9g (8.8% DV)",
            'sodio': "Sodium: 114mg (6% DV)",
            'base_dieta': "*Daily values based on a 2,000 calorie or 8,400kj diet.",
            'atencao_lactose': "Attention: This food CONTAINS LACTOSE",
        }
    },
    '002': {
        'pt': {
            'prato': "\nLASANHA VEGETARIANA",
            'descrição': "Camadas de massa fina intercaladas com molho de tomate caseiro, abobrinha, berinjela e ricota, cobertas com queijo mozzarella derretido. Um prato reconfortante e cheio de sabor, ideal para quem aprecia uma refeição substanciosa e saudável.",
            'lista_ingredientes': "\nIngredientes: Massa de lasanha, tomate, abobrinha, berinjela, ricota, mozzarella, alho, azeite, sal, pimenta e manjericão.",
            'preco_tempo': "\nPreço: R$ 50,00 - Tempo estimado de preparo: 40 minutos",
            'info_nutricional': "\nInformação Nutricional (Porção de 100g):",
            'calorias': "\nValor Calórico: 200kcal (10% VD)",
            'carboidratos': "Carboidratos: 30g (10% VD)",
            'proteinas': "Proteínas: 12g (16% VD)",
            'gorduras': "Gorduras totais: 9g (14% VD)",
            'saturadas': "Gorduras saturadas: 4g",
            'trans': "Gorduras trans: 0g",
            'fibra': "Fibra alimentar: 6g (24% VD)",
            'sodio': "Sódio: 300mg (12% VD)",
            'base_dieta': "*Valores diários com base em dieta de 2.000kcal ou 8.400kj.",
            'atencao_lactose': "Atenção: Este alimento CONTÉM LACTOSE"
        },
        'en': {
            'prato': "\nVEGETARIAN LASAGNA",
            'descricao': "Layers of thin pasta alternated with homemade tomato sauce, zucchini, eggplant, and ricotta, topped with melted mozzarella cheese. A comforting and flavorful dish, perfect for those who enjoy a hearty and healthy meal.",
            'lista_ingredientes': "\nIngredients: Lasagna pasta, tomatoes, zucchini, eggplant, ricotta, mozzarella, garlic, olive oil, salt, pepper, and basil.",
            'preco_tempo': "\nPrice: $ 50.00 - Estimated preparation time: 40 minutes",
            'info_nutricional': "\nNutritional Information (Serving of 100g):",
            'calorias': "\nCaloric Value: 200 kcal (10% DV)",
            'carboidratos': "Carbohydrates: 30g (10% DV)",
            'proteinas': "Proteins: 12g (16% DV)",
            'gorduras': "Total Fats: 9g (14% DV)",
            'saturadas': "Saturated Fats: 4g",
            'trans': "Trans Fats: 0g",
            'fibra': "Dietary Fiber: 6g (24% DV)",
            'sodio': "Sodium: 300mg (12% DV)",
            'base_dieta': "*Daily values based on a 2,000 calorie diet.",
            'atencao_lactose': "Attention: This food CONTAINS LACTOSE"
        }
    }
}

def get_informacoes_prato(codigo_prato, idioma, chave):
    """Retorna as informações do prato com base no código, idioma e chave especificados."""
    prato = cardapio.get(codigo_prato, {})
    if not prato:
        return "Prato não encontrado."
    informacoes = prato.get(idioma, {})
    if not informacoes:
        return "Informações não disponíveis neste idioma."
    return informacoes.get(chave, "Chave não encontrada.")