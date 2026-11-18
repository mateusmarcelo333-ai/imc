
print("----- Plataforma de Leilões e Rastreamento de Gado Bovino -----")

pecuarista = input("Nome do Pecuarista: ").strip().title()
fazenda = input("Nome da Fazenda: ").strip().title()
raca = input("Raça do Animal: ").strip().title()
municipio = input("Município do Registro: ").strip().title()
brinco = input("Código do Brinco Eletrônico: ").strip()
registro = input("Registro Genealógico: ").strip()
peso = input("Peso em Arrobas: ").strip()
idade = input("Idade em Meses: ").strip()
data = input("Data da Pesagem (DD-MM-AAAA): ").strip()
email = input("E-mail da Associação Agropecuária: ").strip()
pin = input("PIN do Produtor: ").strip()

data = data.replace("-", "/")

certificacao = ""

for tentativa in range(5):
    certificacao = input("Certificação Sanitária (APROVADO): ").strip()
    if certificacao == "APROVADO":
        break

if pecuarista.isalpha() and \
fazenda.isalpha() and \
raca.isalpha() and \
municipio.isalpha() and \
brinco.startswith("BOV-") and \
registro.isalnum() and \
peso.isdigit() and \
idade.isdigit() and \
len(data) == 10 and data.count("/") == 2 and \
email.endswith(".agro.org.br") and \
certificacao == "APROVADO":

    print("Dados válidos!")
    print("PIN protegido:", "*" * len(pin))
    print("Animal aprovado para o leilão!")

else:
    print("Dados inválidos!")

print("-" * 30)
