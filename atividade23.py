for tentativas in range(3):
    placa = input("Digite a sua placa: "). strip()

    if len(placa) == 7 and placa != "1234567":
     print("Placa invalida. Chame a segurança")
    break
else:
 print("Placa Registrada. Pode entrar!")