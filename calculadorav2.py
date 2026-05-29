#uma calculadora basica

#funções
def soma(n1, n2):
    print("Vamos somar!")
    resultado = n1 + n2
    print("O resultado é", resultado)


def subtrair(n1, n2):
    print("Vamos subtrair!")
    resultado = n1 - n2
    print("O resultado é", resultado)


def multiplicar(n1, n2):
    print("Vamos multiplicar!")
    resultado = n1 * n2
    print("O resultado é", resultado)


def dividir(n1, n2):
    print("Vamos dividir!")
    
    if n2 ==0:
        print("NÃO da pra dividir por zero seu burro")
    
    else:  
        resultado = n1/n2
        print("O resultado é",resultado)

#while para sempre rodar o programa
while True:
    print("\nVamos calcular")
    print("(1) soma")
    print("(2) subtração")
    print("(3) multiplicação")
    print("(4) divisão")
    print("(5) sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 5:
        print("Saindo da calculadora...")
        break

    elif opcao >= 1 and opcao <= 4:
        if opcao == 1:
            print("\nVamos somar")

        elif opcao == 2:
            print("\nVamos subtrair")

        elif opcao == 3:
            print("\nVamos multiplicar")

        elif opcao == 4:
            print("\nVamos dividir")
        
        n1 = float(input("Digite o primeiro valor: "))
        n2 = float(input("Digite o segundo valor: "))

        if opcao == 1:
            soma(n1, n2)

        elif opcao == 2:
            subtrair(n1, n2)

        elif opcao == 3:
            multiplicar(n1, n2)

        elif opcao == 4:
            dividir(n1, n2)

    else:
        print("Tá vendo alguma opção aí? então kkkkk")