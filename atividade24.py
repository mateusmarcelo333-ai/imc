for tentativas in range(3):
    nome = input("Digite seu nome (deve conter mais de 3 letras)"). strip()
    cidade = input("Diigte a cidade (deve conter mais de 4 letras)"). strip()
    sigla = input("Digite sua sigla"). strip()

    if len (nome) >3 and len(cidade) >=4 and len(sigla) == 2:
        print(f"Seu nome {nome}Sua cidade {cidade}Sua sigla {sigla}")
        break
    else:
        print("Seu nome esta incorreto. Tente novamente!")
else:
 print("Sua cidade esta incorreta. tente novamente")