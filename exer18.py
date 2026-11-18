
print("----- Terminal de Cargas Frigorificadas e Exportação de Carnes -----")

auditor = input("Nome do Auditor Sanitário: ").strip().title()
empresa = input("Empresa Frigorífica: ").strip().title()
corte = input("Tipo de Corte: ").strip().title()
porto = input("Porto de Embarque: ").strip().title()
container = input("Número do Container Reefer: ").strip()
certificado = input("Certificado Internacional: ").strip()
temperatura = input("Temperatura de Congelamento: ").strip()
peso = input("Peso Líquido em Quilos: ").strip()
data = input("Data da Inspeção (DD-MM-AAAA): ").strip()
email = input("E-mail do Ministério da Agricultura: ").strip()
lacre = input("Lacre Eletrônico: ").strip()

data = data.replace("-", "/")

parecer = ""

for tentativa in range(5):
    parecer = input("Parecer de Exportação (LIBERADO): ").strip()
    if parecer == "LIBERADO":
        break

if auditor.isalpha() and \
empresa.isalpha() and \
corte.isalpha() and \
porto.isalpha() and \
container.startswith("REEFER-") and \
certificado.isalnum() and \
temperatura.isdigit() and \
peso.isdigit() and \
len(data) == 10 and data.count("/") == 2 and \
email.endswith(".mapa.gov.br") and \
parecer == "LIBERADO":

    print("Dados válidos!")
    print("Lacre protegido:", "*" * len(lacre))
    print("Exportação liberada!")

else:
    print("Dados inválidos!")

print("-" * 30)
