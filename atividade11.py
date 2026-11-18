senha_correta = "12345"
for tentativas in range(3):
    chute = input("Digite sua senha: ")
    if chute == senha_correta:
        print("Acesso permitido")
        break 
    else:
        print("Senha incorreta!")