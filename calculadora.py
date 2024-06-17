#Calculadora Juros Simples
while True:
    print("\n\t\t\t -- Calculadora Juros Simples")
    
    print("1. Juros")
    print("2. Capital")
    print("3. Taxa")
    print("4. Prazo")
    print("5. Sair")
    
    op=  int(input("\nOpcão: "))
    
    
    if op== 1:
        print("\n\t\t\t -- Juros -- \n")
        
        capital = float(input("informe o Capital: "))
        taxa = float(input("informe a taxa: "))
        tempo = float(input("informe o tempo: "))
        
        juros = (capital * taxa * tempo) / 100
        
        #saída
        print("\n\t\t Juros: {:.2f} = ({} * {} * {}) / 100 \n".format(juros,capital,taxa,tempo))

    if op == 2:
        print("\n\t\t\t -- Capital -- \n")

        #Entrada de dados
        montante = float(input("Informe o montante: "))
        taxa = float(input("Informe a taxa: "))
        tempo = float(input("Informe o tempo: "))

        #Processamento dos dados
        capital = montante / (1 + taxa) * tempo       
        
        #Saída dos dados
        print("\n\t\t {:.5f} = {} / (1 + {}) * {} \n".format(capital,montante,taxa,tempo))
    
    elif op == 5:
        print("\n\nFim da Execução\n\n")
        break
    else:
        if op >= 6:
            print("\n\nOpção {} Incorreta!\n\n".format(op))

        
        
        
        