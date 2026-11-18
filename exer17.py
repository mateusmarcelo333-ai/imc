
print("----- Sistema Central de Emissão de Títulos e Registro Acadêmico Superior -----")

diplomado = input("Nome do Diplomado: ").strip().title()
sobrenome = input("Sobrenome: ").strip().title()
curso = input("Nome do Curso Superior: ").strip().title()
cidade = input("Cidade do Campus: ").strip().title()
diploma = input("Código do Diploma: ").strip()
livro = input("Livro de Registro: ").strip()
carga = input("Carga Horária Cumprida: ").strip()
media = input("Média Geral de Conclusão: ").strip()
data = input("Data da Colação de Grau (DD-MM-AAAA): ").strip()
email = input("E-mail da Reitoria: ").strip()
hash_certificado = input("Código Hash do Certificado Digital: ").strip()

data = data.replace("-", "/")

status = ""

for tentativa in range(5):
    status = input("Status do Diploma (REGISTRADO): ").strip()
    if status == "REGISTRADO":
        break

if diplomado.isalpha() and \
sobrenome.isalpha() and \
curso.isalpha() and \
cidade.isalpha() and \
diploma.startswith("DIP-") and \
livro.isalnum() and \
carga.isdigit() and \
media.isdigit() and \
len(data) == 10 and data.count("/") == 2 and \
email.endswith(".universidade.edu.br") and \
status == "REGISTRADO":

    print("Dados válidos!")
    print("Hash protegido:", "*" * len(hash_certificado))
    print("Diploma registrado com sucesso!")

else:
    print("Dados inválidos!")

print("-" * 30)
