print("----------------------------Sistema de RH-----------------------------")
nome = input("Digite seu cargo (Deve conter 3 letras): ").strip()
cpf = input("Digite a CPF (deve conter 11 caracteres): ").strip()
email = input("Digite sua E-email (Deve conter mais de 10 caracteres): ").strip()
senha = input("Digite sua senha. (Deve conter mais de 8 letras): ").strip()
turno = input("Digite seu turno. (Deve conter mais de 5 letras): ").strip()

if len(nome) >= 3 and len(cpf) == 11 and len(email) > 10 and len(senha) == 8 and len(turno) == 5:
    print(f"Seu nome e {nome}: Seu CPF e {cpf}: Seu E-email e {email}: sua senha e {senha}: seu turno e {turno}:")
else:
    print("Seu nome, CPF, E-mail esta incorreto(a)!. Tente novamente mais tarde")