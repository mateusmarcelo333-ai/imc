senha_correta = "cafe2026"
for tentativas in range(3):
    chute = input("Digite a senha Wi-fi: ")
    if chute == senha_correta:
        print("Wi-fi Liberado")
        break 
    else:
        print("Acesso bloqueado!")