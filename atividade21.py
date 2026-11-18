print("---------- Senha segura ----------")

for tentativas in range(3):
    senha = input("Digite uma senha: ").strip()
    
    if len(senha) >= 8:
        print(f"Senha '{senha}' aceito!")
        break
    else:
        print(f"Senha curto demais: a senha tem que ter 8 caracteristicas")
else:
    print("muitas tentativas.")
    print("-"*20)