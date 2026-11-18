print("---Sturp---")

for tentativa in range(3):

    Agente = input("digite o seu agente:").strip()
    Codinome = input("Digite o seu codinome:").strip()
    Pais = input("Digite o seu pais:").strip()
    ID = input("7 num:").strip()
    Nivel = input("Digite o seu nivel").strip()
    Cargo = input("Digite o seu cargo").strip()
    Especialidade = input("Digite o sua especialidade-")
    Senha = input("Digite a sua senha:").strip()
    Pin = input("4 num").strip()
    Unidade = input("Digite a sua unidade:").strip().upper()
    Superior = input("Digite a sua superior").strip()
    Missão = input("Digite a sua missão:").strip()
    Arma = input("Digite o nome da sua arma:").strip()
    Veiculos = input("Digite o nome do seu carro:").strip()
    Status = input("Digite o seu status").strip().upper()

    if Agente.isalpha() and Agente.isalpha() and \
       Codinome.isalpha() and \
       Pin.isdigit() and \
       ID.isdigit() and \
       len(Unidade) and Unidade.isalpha() == "INTERPOL" and \
       len(Status) and Status.isalpha() == "TOP_SECRET":
        
        print(f"Acesso liberado! Bem-vindo ao sistema, {Agente}.")
        break
else:
    print("SISTEMA BLOQUEADO. Alerta de intrusão enviado à segurança.")