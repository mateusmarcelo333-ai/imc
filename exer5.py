print("-----Sistema de Controle de Imigração-----")

passageiro = input("Nome do Passageiro: ").strip()
sobrenome = input("Sobrenome: ").strip()
pais = input("País de Origem: ").strip()
cidade = input("Cidade de Destino: ").strip()
passaporte = input("Número do Passaporte: ").strip()
voo = input("Código do Voo: ").strip()
bagagem = input("Quantidade de Bagagens: ").strip()
dias = input("Dias de Permanência: ").strip()
data = input("Data de Entrada (DD/MM/AAAA): ").strip()
email = input("E-mail da Companhia Aérea: ").strip()
visto = input("Código do Visto: ").strip()
status = input("Status (AUTORIZADO): ").strip()

if passageiro.isalpha() and \
sobrenome.isalpha() and \
pais.isalpha() and \
cidade.isalpha() and \
passaporte.isalnum() and len(passaporte) == 8 and \
voo.startswith("FLIGHT-") and voo[7:].isalnum() and \
bagagem.isdigit() and \
dias.isdigit() and \
len(data) == 10 and data.count("/") == 2 and \
email.count("@") and email.endswith(".air.com") and \
visto.isalnum() and \
status == "AUTORIZADO":

    print("Entrada autorizada!")
else:
    print("Dados inválidos!")

print("-" * 30)