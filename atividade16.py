for tentativa in range(6):

    Peso = int(input(f"Qual seu peso? "))

    if   Peso <= 40:
     print("Pode balançar!")
    else:
     print("Peso acima do limite! ")