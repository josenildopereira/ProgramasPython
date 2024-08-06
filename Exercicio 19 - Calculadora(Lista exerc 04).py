# Obs.: Use o Pycharm para a exibição de cores aparecer perfeita

valor1 = float(input('\nDigite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor : '))
opcao = int
resultado = 0

while opcao != 0:
    try: # Esse try é para impedir que o usuario escolha uma letra ao inves da opçõa.
        print('\n*************************************')
        print('''        [ 1 ] - SOMAR 
        [ 2 ] - SUBTRAIR
        [ 3 ] - MULTIPLICAR
        [ 4 ] - DIVIDIR
        [ 0 ] - SAIR DO PROGRAMA''')
        print('*************************************')
        opcao = int(input('Escolha a operação: '))

        if opcao == 1:
            resultado = valor1 + valor2
            print(f'\n\033[34mA soma dos numeros é: {resultado}\033[38m')

        elif opcao == 2:
            resultado = valor1 - valor2
            print(f'\n\033[34mA diferença dos numeros é: {resultado}\033[38m')

        elif opcao == 3:
            resultado = valor1 * valor2
            print(f'\n\033[34mO produto dos numeros é: {resultado}\033[38m')

        elif opcao == 4:
            resultado = valor1 / valor2
            print(f'\n\033[34mA divisão dos numeros é: {resultado:.2f}\033[38m')

        elif opcao == 0:
            print('\n\033[33mEncerrando programa!!!\033[38m')
        else:
            print('\n\033[31mOpção inválida. Tente novamente:\033[38m')

    except ValueError:
        print('\n\033[031mOpção inválida. Tente Novamente\033[038m')