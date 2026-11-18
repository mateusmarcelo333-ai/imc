
print("----- Auditoria Forense Digital e Custódia de Evidências -----")

perito = input("Nome do Perito: ").strip().title()
especialidade = input("Especialidade Forense: ").strip().title()
departamento = input("Departamento Policial: ").strip().upper()
cidade = input("Cidade da Ocorrência: ").strip().title()
evidencia = input("Código da Evidência: ").strip()
hash_sha = input("Hash SHA-256 da Imagem: ").strip()
tamanho = input("Tamanho em Megabytes: ").strip()
lacre = input("Número do Lacre: ").strip()
data = input("Data da Apreensão (DD-MM-AAAA): ").strip()
email = input("E-mail do Instituto de Perícia: ").strip()
senha = input("Senha do Cofre Digital: ").strip()

data = data.replace("-", "/")

parecer = ""

for tentativa in range(5):
    parecer = input("Parecer Forense (INTEGRO): ").strip()
    if parecer == "INTEGRO":
        break

if perito.isalpha() and \
especialidade.isalpha() and \
departamento == departamento.upper() and \
cidade.isalpha() and \
evidencia.startswith("EVID-") and \
hash_sha.isalnum() and \
tamanho.isdigit() and \
lacre.isdigit() and \
len(data) == 10 and data.count("/") == 2 and \
email.endswith(".policia.gov.br") and \
parecer == "INTEGRO":

    print("Dados válidos!")
    print("Senha protegida:", "*" * len(senha))
    print("Custódia de evidências autorizada!")

else:
    print("Dados inválidos!")

print("-" * 30)
