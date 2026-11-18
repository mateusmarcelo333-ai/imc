print("----------Seguranças em duas etapas----------")
codigo_correto = "100"
senha_correta = "mateus"
for tentativas in range(3):
    chute = input("Digite o codigo de area:")
    senha= input("digite sua senha:")
    if chute == senha_correta or chute == codigo_correto:
        print("Codigo correto! entrando...")
        break
    else:
        print("Senha, Incorreto!.")
else:
    print("muitas falhas.conta bloqueada")
    print("-"*30)