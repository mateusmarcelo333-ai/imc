senha = input("Digite sua senha: ").strip()

if len(senha) < 8:
    print("Sua senha é curta demais")
else:
    print("Senha aceita.")