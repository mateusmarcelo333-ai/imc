print("----------------------------Sistema de Hotel-----------------------------")
Hóspede = input("Digite o seu pais, e hóspede (Deve conter 3 letras): ").strip()
passaporte = input("Digite seu passaporte (deve conter exatamente 6 digitidos): ").strip()
quarto = input("Digite o numero do seu quarto (Deve conter exatamente 3 digitidos): ").strip()
Data = input("Digite a Data (Deve conter exatamente 8 digitidos): ").strip()
Código = input("Digite um codigo diferente de '0000'. ").strip()
if len(Hóspede) >= 3 and len(passaporte) == 6 and len(quarto) > 3 and len(Data) == 8 and len(Código) == 4:
    print(f"Hospede {Hóspede}: Seu passaporte e {passaporte}: Seu quarto e {quarto}: sua data e {Data}: codigo diferente de '0000'{Código}:")
else:
    print("Seu nome, passaporte, seu quarto, seu codigo esta incorreto(a)!. Tente novamente mais tarde")