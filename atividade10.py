senha_correta = "12345"
email_extra = "admin@email.com"
for tentativas in range(3):
    chute = input("Digite a senha (ou e-mail de acesso): ")
    if chute == senha_correta or chute == email_extra:
        print("Acesso Liberado!")
        break
    else:
        print("Incorreto!.")
else:
    print("Conta bloqueada.")