print("---Controle de retor de fusao nuclear---")

for tentativa in range(3):
    
    Reator = input("Digite o seu reator:").strip()
    Elemento = input("Digite o seu elemento:").strip()
    Massa = input("Digite a sua massa:").strip()
    Calor = input("Digite o seu calor:").strip()
    Pressão = input("Digite a sua pressão:").strip()
    Fluxo = input("Digite o seu fluxo:").strip()
    Técnico = input("Digite o seu nivel de tecnico:").strip()
    ID_TEC = input("5 num").strip()
    Turno = input("Digite o seu turno:").strip()
    Estação = input("Digite a sua estação:").strip()
    Resfriamento = input("Digite o seu resfriamento:").strip()
    Energia = input("Digite a sua energia:").strip()
    Status = input("Digite o seu status:").strip().upper()
    Emergencia = input("Digite a sua emergrncia:").strip().upper()
    Chave = input("Digite a sua chave:").strip()

    if Reator.isalpha() and Reator.isalpha() and \
       Elemento.isalpha() and \
       Técnico.isalpha() and \
       Calor.isdigit() and \
       Pressão.isdigit() and \
       ID_TEC.isdigit() and \
       len(Status) and Status.isalpha() == "ESTAVEL" and \
       len(Emergencia) and Emergencia.isalpha() == "DESATIVADA":
        
        print(f"Acesso liberado! Bem-vindo ao sistema, {Reator}.")
        break
else:
    print("SISTEMA BLOQUEADO. Alerta de intrusão enviado à segurança.")