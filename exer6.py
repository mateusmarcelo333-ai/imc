
print("----- Gestão de Cargas e Tráfego Ferroviário de Minérios -----")

maquinista = input("Nome do Maquinista: ").strip().title()
partida = input("Terminal de Partida: ").strip().title()
chegada = input("Terminal de Chegada: ").strip().title()
minerio = input("Tipo de Minério: ").strip().title()
vagao = input("Código do Vagão: ").strip()
trem = input("Número do Trem: ").strip()
peso = input("Peso em Toneladas: ").strip()
km = input("Quilômetros a Percorrer: ").strip()
data = input("Data da Viagem (DD-MM-AAAA): ").strip()
email = input("E-mail da Ferrovia: ").strip()
chave = input("Chave do Bloqueio de Freio: ").strip()

data = data.replace("-", "/")

sinalizacao = ""

for tentativa in range(5):
    sinalizacao = input("Sinalização da Linha (VERDE): ").strip()
    if sinalizacao == "VERDE":
        break

if maquinista.isalpha() and \
partida.isalpha() and \
chegada.isalpha() and \
minerio.isalpha() and \
vagao.startswith("CARGA-") and \
trem.isalnum() and \
peso.isdigit() and \
km.isdigit() and \
len(data) == 10 and data.count("/") == 2 and \
email.endswith(".ferrovia.log.br") and \
sinalizacao == "VERDE":

    print("Dados válidos!")
    print("Chave protegida:", "*" * len(chave))
    print("Tráfego ferroviário autorizado!")

else:
    print("Dados inválidos!")

print("-" * 30)
