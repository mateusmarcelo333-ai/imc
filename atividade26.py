for tentativas in range(3):
 nome = input("Digite seu nome (Deve conter mais de 6 letras): "). strip()
 senha = input("Digite a senha (deve conter 4 caracteres): "). strip()
 frase = input("Digite sua frase. (Deve conter mais de 10 caracteres): "). strip()

 if len(nome) >= 3 and len(senha) >4 and len(frase) > 10:
     print(f"Seu nome e {nome} Sua senha e (senha) Sua frase e {frase} ")
     break
else:
 print("Seu nome, senha ou frase esta incorreto(a)!. Tente novamente mais tarde") 