def ler_vetor():

    #Leitura dos vetores
    vetor = []
    for i in range(5): 
        elemento = int(input(f"Digite o {i+1}º elemento: "))
        vetor.append(elemento)
    return vetor

def calcular_resultado(vetorA, vetorB): 

    #Calculo do vetor

    vetorC = []
    for i in range(5): 
        if (vetorA[i] % 2 == 0):
            vetorC.append(vetorA[i] * vetorB[i])
        else: 
            vetorC.append(vetorA[i])  
    return vetorC

def imprimir_vetor(vetor, nome):
    print(f"Vetor {nome}: {vetor}")

while True: 
    print("===========Menu============")
    print("1. Ler vetores A e B")
    print("2. Calcular vetor C")
    print("3. Sair")
    print("===========================")

    opcao = input("Escolha uma opção: ")

    if opcao == '1': 
        vetor_a = ler_vetor()  
        vetor_b = ler_vetor()  
        imprimir_vetor(vetor_a, 'A')
        imprimir_vetor(vetor_b, 'B')
    elif opcao == '2': 
        try:
            vetor_c = calcular_resultado(vetor_a, vetor_b)
            imprimir_vetor(vetor_c, 'C')
        except NameError:

            #Verificar ERRO
            print("Você precisa ler os vetores A e B primeiro!")
        except IndexError:

            #Verificar ERRO/
            print("Erro: Os vetores A e B devem ser lidos antes de calcular o vetor C.")
    elif opcao == '3': 
        print("Saindo do programa...")
        break
