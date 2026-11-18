print("---------- login de usuario ----------")

for tentativas in range(3):
    usuario = input("Digite seu nome: ").strip()
    
    if len(usuario) >= 5:
        print(f"Usuário '{usuario}' aceito!")
        break
    else:
        print(f"Nome curto demais:")
else:
    print("muitas tentativas.")
    print("-"*20)