largura = int(input("informe a largura: "))
altura = int(input("informe a altura: "))
quantidade = int(input("informe a quantidade: "))

while quantidade > 0:
    quantidade = quantidade - 1

    lagCliente = int(input("informe a largura: "))
    altCliente = int(input("informe a altura: "))

    if ( largura * altura) >= (lagCliente * altCliente):
        print("Sim")
    else:
        print("Não")
