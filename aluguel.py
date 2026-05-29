def menu():

    print("Aluguel de carros")

    print("(1) carro popular")
    print("(2) carro de luxo")
    opção = int(input("Deseja qual opção: "))
    dias = int(input("Quantos dias alugado? "))
    km = float(input("Quantos Km foram percorridos? "))


    # carro popular
    if opção == 1:
        aluguel = dias * 90

        if km <= 100:
            km_valor = km * 0.20
        else:
            km_valor = km * 0.10

        preco = aluguel + km_valor

    # carro de luxo
    elif opção == 2:
        aluguel = dias * 150

        if km <= 200:
            km_valor = km * 0.30
        else:
            km_valor = km * 0.25

        preco = aluguel + km_valor

    print(f"O preço total será R${preco:.2f}")


menu()