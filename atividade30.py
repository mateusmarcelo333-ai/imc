Proprietario = input("Digite o seu nome (Deve conter 7 letras): ").strip()
Modelo = input("Digite o Modelo do seu carro (deve conter exatamente 7 digitidos): ").strip()
cor = input("Digite a cor do seu carro (Deve conter exatamente 7 digitidos): ").strip()
Placa = input("Digite a placa do seu carro (Deve conter exatamente 7 digitidos): ").strip()
chassi = input("Digite o codigo do seu chassi(Deve conter 10 caracteristicas)").strip()
Ano = input("Digite o ano do seu carro(deve conter exatamente 4 numeros)")
if len(Proprietario) >= 7 and len(Modelo) == 7 and len(cor) > 7 and len(Placa) == 7 and len(chassi) == 10 and len(Ano)== 4:
    print(f"Seu nome e {Proprietario}: Seu Modelo e{Modelo}: Sua cor e {cor}: sua Placa e{Placa}: Codigo do seu chassi{chassi}:Ano do seu carro{Ano}")
else:
    print("Sua placa esta errada, modelo de carro errado, codigo do chassi errado,Ano do seu carro esta errado,seu codigo esta incorreto(a)!. Tente novamente mais tarde")