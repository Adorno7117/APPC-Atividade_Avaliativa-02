tabelaFuncionario = {}

def exibir_menu():   
    print(36 * "\n\n=")
    print("\t\tMenu:")
    print(36 * "=")
    print("1. Inserir funcionario")
    print("2. Remover Funcionario")
    print("3. Determinar folha de pagamento")
    print("4. Determinar relatorio de funcionarios")
    print("5. Funcionario com maior salario líquido")
    print("6. Funcionario com mais faltas")
    print("7. Listar todos os funcionários")
    print("0. Sair")
    print(36 * "=")

def calcula_desconto(salarioFixo, numFalta):
    if salarioFixo <= 2259.20:
        salarioLiq = salarioFixo - ((salarioFixo / 30) * numFalta)
        imposto = 0
    elif salarioFixo <= 2828.65:
        salarioLiq = salarioFixo - ((salarioFixo - ((salarioFixo / 30) * numFalta)) * 0.075)
        imposto = 7.5
    elif salarioFixo <= 3751.05:
        salarioLiq = salarioFixo - ((salarioFixo - ((salarioFixo / 30) * numFalta)) * 0.15)
        imposto = 15
    elif salarioFixo <= 4664.68:
        salarioLiq = salarioFixo - ((salarioFixo - ((salarioFixo / 30) * numFalta)) * 0.225)
        imposto = 22.5
    else:
        salarioLiq = salarioFixo - ((salarioFixo - ((salarioFixo / 30) * numFalta)) * 0.275)
        imposto = 275
    
    return [imposto, salarioLiq]

def adicionar_funcionario():
    matricula = int(input("\nDigite o número da matricula: "))
    
    while matricula in tabelaFuncionario.keys():
        print("\nMatricula Invalida!")
        matricula = int(input("Digite um número de matricula válido: "))
        
    nome = str(input("Digite o nome do funcionario: "))
    
    print("\n\t\tMenu:")
    print(36 * "=")
    print("101. Vendedor")
    print("102- Administrativo")
    print(36 * "-")
    codigo = int(input("\nDigite o codigo: "))
    
    while codigo not in [101, 102]:
        print("\nCodigo Invalido!")
        codigo = int(input("Digite um codigo válido: "))
    
    numFalta = int(input("Digite o número de faltas: "))
    
    if codigo == 101:
        valorVenda = float(input("Digite o valor de vendas/mês do vendedor: R$ "))
        salarioFixo = 1500 + (valorVenda * 0.09)
        
    else:
        salarioFixo = float(input("Digite o Salario Fixo do funcionário: "))
        
        
        while salarioFixo < 2150.00 or salarioFixo > 6950.00:
            print("\nSalário Invalido!")
            salarioFixo = float(input("Digite um Salario Fixo válido: "))
        
    # Calcula imposto e salario liquido funcionario
    impostoAndSalarioLiq = calcula_desconto(salarioFixo, numFalta)
    
    tabelaFuncionario[matricula] = {
        "nome": nome,
        "codigo": codigo,
        "numero_faltas": numFalta,
        "salario_bruto": salarioFixo,
        "salario_liquido": impostoAndSalarioLiq[1],
        "imposto": impostoAndSalarioLiq[0],
    }
    print(f"Funcionario {nome} inserido com sucesso!")
    print(tabelaFuncionario[matricula])

def remover_funcionario ():
    matricula = int(input('\nDigite o número da matricula do funcionario a ser removido: '))

    if matricula in tabelaFuncionario:
        opcao = input('\nDeseja realmente excluir este funcioario? s[SIM] n[NÃO]: ').upper()
        
        while opcao not in ['S', 'N']:
            opcao = input('\nDeseja realmente excluir este funcioario? s[SIM] n[NÃO]: ').upper()
        
        if opcao == 'S':
            print(f"Funcionário {tabelaFuncionario[matricula]['nome']} removido com sucesso!")
            del tabelaFuncionario[matricula]

    else:
        print(f"Não foi possivel encontrar um funcionário com a matricula {matricula}")
        
def folha_pagamento (): 
    matricula = int(input("\nDigite o número da matricula: "))
    
    if matricula in tabelaFuncionario:
        setorFuncionario = ''
        
        if tabelaFuncionario[matricula]['codigo'] == 101:
            setorFuncionario = 'Vendendor'
        else:
            setorFuncionario = 'Administrativo'
            
        print("Nome da empresa: Marketing é Tudo")
        
        print(f"\n{'Matricula':<10} {'Nome':<20} {'Setor':<25} {'Salário Bruto':<15} {'Salário Líquido':<18} {'Descontos':<10} {'Imposto':<10}")
        print("-" * 110)
        print(f"{matricula:<10} {tabelaFuncionario[matricula]['nome']:<20} {tabelaFuncionario[matricula]['codigo']:<3} - {setorFuncionario:<20} R$ {tabelaFuncionario[matricula]['salario_bruto']:<14.2f} R$ {tabelaFuncionario[matricula]['salario_liquido']:<14.2f} {(tabelaFuncionario[matricula]['salario_bruto'] - tabelaFuncionario[matricula]['salario_liquido']):<10} {tabelaFuncionario[matricula]['imposto']} %")

        
    else:
        print(f"Não foi possivel encontrar um funcionário com a matricula {matricula}")
         
def relatorio_funcionario():
    print(f"\n{'Matricula':<10} {'Nome':<20} {'Código':<10} {'Salário Bruto':<15} {'Salário Líquido':<15}")
    print("-" * 90)
    for matricula, dados in tabelaFuncionario.items():
        print(f"{matricula:<10} {dados['nome']:<20} {dados['codigo']:<10} R$ {dados['salario_bruto']:<14.2f} R$ {dados['salario_liquido']:<14.2f}")
         
def maiorSalarioLiquido():
    matriculaFuncionario = 0
    maiorSalario = 0

    print(f"\n{'Matricula':<10} {'Nome':<20} {'Código da Função':<20} {'Número de Faltas':<18} {'Salário Bruto':<15} {'Salário Líquido':<18} {'Imposto':<10}")
    print("-" * 116)

    for matricula, dados in tabelaFuncionario.items():
        if dados['salario_liquido'] > maiorSalario:
            maiorSalario = dados['salario_liquido']
            matriculaFuncionario = matricula

    print(f"{matriculaFuncionario:<10} {tabelaFuncionario[matriculaFuncionario]['nome']:<20} {tabelaFuncionario[matriculaFuncionario]['codigo']:<20} {tabelaFuncionario[matriculaFuncionario]['numero_faltas']:<18} R$ {tabelaFuncionario[matriculaFuncionario]['salario_bruto']:<14.2f} R$ {tabelaFuncionario[matriculaFuncionario]['salario_liquido']:<14.2f} {tabelaFuncionario[matriculaFuncionario]['imposto']:<10}%")
            
def maiorNumFaltas():
    matriculaFuncionario = 0
    faltas = -1

    print(f"\n{'Matricula':<10} {'Nome':<20} {'Código da Função':<20} {'Número de Faltas':<18} {'Desconto Salário':<15}")
    print("-" * 116)

    for matricula, dados in tabelaFuncionario.items():
        if dados['numero_faltas'] > faltas:
            faltas = dados['numero_faltas']
            matriculaFuncionario = matricula
                  
    desconto = tabelaFuncionario[matriculaFuncionario]['salario_bruto'] - tabelaFuncionario[matriculaFuncionario]['salario_liquido']

    print(f"{matriculaFuncionario:<10} {tabelaFuncionario[matriculaFuncionario]['nome']:<20} {tabelaFuncionario[matriculaFuncionario]['codigo']:<20} {tabelaFuncionario[matriculaFuncionario]['numero_faltas']:<18} R$ {(desconto):<14.2f} ")
        
while True:
    exibir_menu()
    
    opcaoMenu = int(input('Escolha uma opção: '))

    if opcaoMenu == 1:
        adicionar_funcionario()
    elif opcaoMenu == 2:
        remover_funcionario()
    elif opcaoMenu == 3:
        folha_pagamento()
    elif opcaoMenu == 4:
        relatorio_funcionario()
    elif opcaoMenu == 5:
        maiorSalarioLiquido()
    elif opcaoMenu == 6:
        maiorNumFaltas()
    elif opcaoMenu == 7:
        print(tabelaFuncionario)
    elif opcaoMenu == 0:
        break
    else:
        print("\n Opção inválida. Tente novamente. \n ")

print("\nPrograma Encerrado")