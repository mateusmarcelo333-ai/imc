senha_correta = "1234"
for tentativas in range(4):
    chute = input("Digite sua senha: ")
    if chute == senha_correta:
        print("Aparelho Desploqueado")
        break 
    else:
        print("Celular Inoperante por 30 minutos!")