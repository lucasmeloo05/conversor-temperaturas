# Função para converter a temperatura de um tipo para outro
def converter_temperatura(tipo_temperatura, temperatura, converter_para):
    if tipo_temperatura == 'C': # Se a temperatura estiver em Celsius
        if converter_para == 'F': # Converter para Fahrenheit
            return temperatura * 9 / 5 + 32
        elif converter_para == 'K': # Converter para Kelvin
            return temperatura + 273
    elif tipo_temperatura == 'F': # Se a temperatura estiver em Fahrenheit
        if converter_para == 'C': # Converter para Celsius
            return (temperatura - 32) * 5 / 9
        elif converter_para == 'K': # Converter para Kelvin
            return (temperatura - 32) * 5 / 9 + 273
    elif tipo_temperatura == 'K': # Se a temperatura estiver em Kelvin
        if converter_para == 'C': # Converter para Celsius
            return temperatura - 273
        elif converter_para == 'F': # Converter para Fahrenheit
            return (temperatura - 273) * 9 / 5 + 32
    # Se os tipos de temperatura ou conversão forem inválidos, o usuário terá que repetir
    raise ValueError('Tipo de temperatura ou conversão inválidos')

# Loop principal
while True:
    try:
        # Perguntar ao usuário qual tipo de temperatura deseja escolher para iniciar
        while True:
            try:
                tipo_temperatura = input('Qual tipo de temperatura deseja escolher?\nCELSIUS [C]\nFAHRENHEIT [F]\nKELVIN [K]\nESCOLHA: ').strip().upper()[0]
                if tipo_temperatura not in ['C', 'F', 'K']:
                    raise ValueError('Tipo de temperatura inválido')
                break
            except ValueError:
                print('Por favor, digite uma opção válida')

        # Loop para garantir que o usuário digite um número para a temperatura
        while True:
            try:
                temperatura_str = input(f'Qual a temperatura em {tipo_temperatura}: ')
                temperatura_str = temperatura_str.replace("°", "")  # remove o símbolo de graus, caso exista
                temperatura_str = temperatura_str.replace(",", ".")  # substitui "," por ".", caso o usuário digite a temperatura no padrão brasileiro
                temperatura = float(temperatura_str)
                break  # Sai do loop se a conversão for correta
            except ValueError:
                print('Por favor, digite um número válido para a temperatura')

        # Perguntar para qual tipo de temperatura o usuário deseja converter
        while True:
            try:
                converter_para = input('Para qual temperatura deseja converter?\nCELSIUS [C]\nFAHRENHEIT [F]\nKELVIN [K]\nESCOLHA: ').strip().upper()[0]
                if tipo_temperatura == converter_para:
                    print('Mesmo tipo de temperatura, tente novamente')
                if converter_para not in ['C', 'F', 'K']:
                    raise ValueError('Tipo de temperatura inválido')
                break
            except ValueError:
                print('Por favor, digite uma opção válida')

        # Resposta do programa
        temperatura_convertida = converter_temperatura(tipo_temperatura, temperatura, converter_para)
        print(f'{temperatura:.1f}° {tipo_temperatura} correspondem a {temperatura_convertida:.1f}° {converter_para}')
    except ValueError as e:
        print(f'Entrada inválida: {e}')

    # Perguntar ao usuário se ele deseja fazer uma nova conversão ou encerrar o aplicativo
    while True:
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if continuar not in ['S', 'N']:
            print('Entrada inválida, tente novamente')
        else:
            break
    if continuar == 'N':
        print('PROGRAMA ENCERRADO')
        break
