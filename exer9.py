
print("----- Centro de Comando e Telemetria de Drones de Resgate -----")

piloto = input("Nome do Piloto Remoto: ").strip().title()
regiao = input("Região de Busca: ").strip().title()
cidade = input("Cidade Base: ").strip().title()
missao = input("Tipo de Missão: ").strip().title()
prefixo = input("Prefixo do Drone: ").strip()
canal = input("Canal do Transmissor: ").strip()
altitude = input("Altitude de Voo: ").strip()
bateria = input("Nível da Bateria em Porcentagem: ").strip()
data = input("Data da Decolagem (DD-MM-AAAA): ").strip()
email = input("E-mail do Corpo de Bombeiros: ").strip()
chave = input("Chave de Arme dos Motores: ").strip()

data = data.replace("-", "/")

status = ""

for tentativa in range(5):
    status = input("Status do Link (CONECTADO): ").strip()
    if status == "CONECTADO":
        break

if piloto.isalpha() and \
regiao.isalpha() and \
cidade.isalpha() and \
missao.isalpha() and \
prefixo.startswith("DRONE-") and \
canal.isalnum() and \
altitude.isdigit() and \
bateria.isdigit() and \
len(data) == 10 and data.count("/") == 2 and \
email.endswith(".bombeiros.gov.br") and \
status == "CONECTADO":

    print("Dados válidos!")
    print("Chave protegida:", "*" * len(chave))
    print("Telemetria validada!")

else:
    print("Dados inválidos!")

print("-" * 30)
