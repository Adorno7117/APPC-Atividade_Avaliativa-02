tabela_funcionario = {}
menu = int(input('''\n\t 
                    --------------------------------------
                    |     DIGITE A OPÇÃO QUE DESEJAR!    |
                    --------------------------------------
                 
        1- Inserir funcionario              2- Remover Funcionario

        3- Determinar folha de pagamento    4- Determinar relatorio de salario
          
        5- Funcionario maior salario        6- Funcionario mais faltas 
                            
                                  0- Sair\n\t\t'''))

while menu!= 0:

    #Inserir funcionario
    if menu == 1:
        matricula = int(input('\n\tDigite o numero da matricula: '))
        while matricula in tabela_funcionario:
            print('\n\tMatricula Invalida!')
            matricula = int(input('\n\tDigite outro numero da matricula: '))
        nome = str(input('\n\tDigite o nome do funcionario: '))
        cod = int(input('\n\tDigite o codigo: '))
        while  cod not in [101, 102]:
            print('\n\tCodigo Invalido!')
            cod = int(input('\tDigite o codigo correto: '))
        numF = int(input('\n\tDigite o numero de faltas: '))
        if cod == 101:
            valorVendas= float(input('\tDigite o valor de vendas/mês do vendedor: R$'))
            salFixo = 1500 + (valorVendas* 0.09)
        else:
            salFixo = float(input('\n\tDigite Salario Fixo: '))
            while salFixo < 2150 and salFixo > 6950:
                print('\nSalário Invalido!')
                salFixo = float(input('\tDigite Salario Fixo Correto: '))
                if salFixo > 2150 and salFixo < 6950:
                    break
        print(salFixo)
        #Verificação de salarios
        if salFixo<0:
            print('Erro: salario inferior a zero')
            continue
        elif  salFixo > 0 and salFixo < 2259.20:
            salLiq = salFixo - ((salFixo/30) * numF)
            imposto = 0
        elif  salFixo > 2259.21 and salFixo < 2828.65:
            salLiq = salFixo - ((salFixo - ((salFixo/30) * numF)) * 0.075)
            imposto = 7,5
        elif  salFixo > 2828.66 and salFixo < 3751.05:
            salLiq = salFixo - ((salFixo - ((salFixo/30) * numF)) *  0.15)
            imposto = 15
        elif  salFixo > 3751.06 and salFixo < 4664.68:
            salLiq =salFixo - ((salFixo - ((salFixo/30) * numF)) *  0.225)
            imposto = 22,5
        else:
            salLiq = salFixo - ((salFixo - ((salFixo/30) * numF)) *  0.275) 
            imposto = 2,75

        tabela_funcionario[matricula] = {
            'nome': nome,
            'codigo': cod,
            'numero_faltas': numF,
            'salario_bruto': salFixo,
            'salario_liquido': salLiq,
            'imposto': imposto
        }
        print(f'Funcionario {nome} inserido com sucesso!')
        print(tabela_funcionario[matricula])
        
    #Remove funcionario
    elif menu == 2:
        matricula = int(input('\n\tDigite o numero da matricula do funcionario a ser removido: '))
        if matricula in tabela_funcionario:
            menuEX = str(input('\n\tDeseja realmente excluir este funcioario? s[SIM] n[NÃO]\n'))
            if menuEX == 's' or 'S':
                del tabela_funcionario[matricula]
                print(f'Funcionario {matricula} removido com sucesso!')
            else:
                print('Função cancelada')
        else:
            print(f'Funcionario com matricula {matricula} nao encontrado.')
    #Determinar folha de pagamento 
    elif menu == 3:
        print(f"\n{'Matricula':<10} {'nome':<20} {'codigo':<10} {'numero_faltas':<15} {'salario_bruto':<15} {'salario_liquido':<18} {'imposto':<10}")
        print("-" * 90)
        for matricula, dados in tabela_funcionario.items():
            print(f"{matricula:<10} {dados['nome']:<20} {dados['codigo']:<10} {dados['numero_faltas']:<15} R$ {dados['salario_bruto']:<14.2f} R$ {dados['salario_liquido']:<14.2f} {dados['imposto']:<10}%")
    #Determinar relatorio de salario
    elif menu == 4:
        print(f"\n{'Matricula':<10} {'nome':<20} {'codigo':<10} {'salario_bruto':<15} {'salario_liquido':<15}")
        print("-" * 90)
        for matricula, dados in tabela_funcionario.items():
            print(f"{matricula:<10} {dados['nome']:<20} {dados['codigo']:<10} R$ {dados['salario_bruto']:<14.2f} R$ {dados['salario_liquido']:<14.2f}")
    #Funcionario maior salario
    elif menu == 5:
        pass
    #Funcionario mais faltas 
    elif menu == 6:
        pass

    else:
        print('Digite uma opçã valida!')



    menu = int(input('''\n\t 
                    --------------------------------------
                    |     DIGITE A OPÇÃO QUE DESEJAR!    |
                    --------------------------------------
                     
        1- Inserir funcionario              2- Remover Funcionario

        3- Determinar folha de pagamento    4- Determinar relatorio de salario
          
        5- Funcionario maior salario        6- Funcionario mais faltas 
                            
                                  0- Sair\n\t\t'''))

print("\nPrograma Encerrado")