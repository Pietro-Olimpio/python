def reajuste():

    print("Reajuste salarial")
    print("(1) mulheres")
    print("(2) homens")
    opção = int(input("deseja qual opção:"))
    salario = float(input("Digite o salário atual: R$"))
    anos = int(input("Quantos anos trabalha na empresa? "))

    # Mulheres
    if opção == 1:

        if anos < 5:
            aumento = salario * 0.04

        elif anos <= 10:
            aumento = salario * 0.07

        elif anos <= 20:
            aumento = salario * 0.12

        else:
            aumento = salario * 0.23

    # Homens
    elif opção == 2:

        if anos < 5:
            aumento = salario * 0.03

        elif anos <= 15:
            aumento = salario * 0.08

        elif anos <= 30:
            aumento = salario * 0.14

        else:
            aumento = salario * 0.25

    novo_salario = salario + aumento

    print(f"Novo salário: R${novo_salario:.2f}")


reajuste()