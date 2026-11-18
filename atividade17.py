for tentativa in range(10):

    Peso = int(input(f"Quantidade de roupas? "))

    if   Peso <= 5:
     print("Venda realizada!")
    else:
     print("Quantidade indisponivel no estoque! ")