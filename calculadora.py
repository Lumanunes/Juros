#Calculadora Juros Simples
while True:
    print("\n\t\t\t -- Calculadora Juros Simples")
    
    print("1. Juros")
    print("2.Capital")
    print("3.Taxa")
    print("4.Prazo")
    print("5.Sair")
    
    op=  int(input("\nOpcão: "))
    
    
    if op== 1:
        print("\n\t\t\t -- Juros -- \n")
        
        capital = float(input("informe o Capital: "))
        taxa = float(input("informe a taxa: "))
        tempo = float(input("informe o tempo: "))
        
        juros = (capital * taxa * tempo) / 100
        
        #saída
        print("\n\t\t Juros:{:.2f} = ({} * {} * {}) / 100 \n".format(juros,capital,taxa,tempo))
        
        
        
        