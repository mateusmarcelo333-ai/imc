print("--- Sistema de auditoria ---")

for tentativa in range(3):
    Máquina = input("Digite o nome da máquina:")
    Série = input("Digite a sua série:")
    Operador = input("Digite o seu nome de Operador:")
    Turno = input("Digite o seu turno de trabalho:")
    Pecas_Dia = input("Digite o numero da pecas:")
    Defeitos = input("Digite o numero do defeito:")
    Email_T = input("Digite o seu Email_t:")
    Fabrica = input("Qual eo nome da fabrica:")
    Setor = input("Digite o seu setor:")
    Corredor = input("Digite o seu corredor:")
    Gaveta = input("Digite o numero da sua gaveta:")
    Fornecedor = input("Digite o seu Fornecedor:")
    CNPJ_F = input("Digite o seu cnpj (14 num):")
    Data_Manut = input("Data precissa de 2 // (DD/MM/AAAA)")
    Status = input("Status deve ser OPERACIONAL:")

    if Setor.isalpha() and \
       Fornecedor.isalpha() and \
       Pecas_Dia.isdigit() and \
       Defeitos.isdigit() and \
       Gaveta.isdigit() and \
       CNPJ_F.isdigit() and \
       Série.isalnum() and \
       Email_T.count("@") == 1 and Email_T.endswith(".com") and \
       Data_Manut.count("/") == 2 and \
       Status == "OPERACIONAL":
        
         print(f"\nSUCESSO Status {Operador}, seu {CNPJ_F} foi enviado!")
         break
    else:
          print(f"\nERRO: Dados invalidos! Tentativa {tentativa + 1} de 3.")
          print("-" * 40)
else:
          print("f\n Bloqueado: muitas falhas. procura o diretor de segurança.")