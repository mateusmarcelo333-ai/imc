print("--- Sistema de auditoria ---")

for tentativa in range(3):

    Aluno = input("Digite o nome do aluno: ")
    CPF = input("Digite o seu CPF (apenas 11 números): ")
    RG = input("Digite o seu RG (apenas números): ")
    idade = input("Digite a sua idade (apenas números): ")
    Curso = input("Digite o seu curso: ")
    Semestre = input("Digite o seu semestre (número): ")
    Turno = input("Digite o turno: ")
    Campus = input("Digite o campus: ")
    Email_A = input("Digite o e-mail do aluno: ")
    RA = input("Digite o RA (6 números): ")
    Bolsista = input("Bolsista? (SIM/NÃO): ").upper()
    Coodernador = input("Digite o nome do coordenador: ")
    Telefone = input("Digite o telefone (apenas números): ")
    Data_Matriculas = input("Data (DD/MM/AAAA): ")
    Status = input("Digite o status: ").upper()

    if Aluno.replace(" ", "").isalpha() and \
       Coodernador.replace(" ", "").isalpha() and \
       Curso.replace(" ", "").isalpha() and \
       Campus.replace(" ", "").isalpha() and \
       CPF.isdigit() and len(CPF) == 11 and \
       RG.isdigit() and \
       idade.isdigit() and \
       Semestre.isdigit() and \
       RA.isdigit() and len(RA) == 6 and \
       Telefone.isdigit() and \
       Data_Matriculas.count("/") == 2 and \
       Email_A.count("@") == 1 and Email_A.endswith(".com") and \
       Bolsista in ["SIM", "NÃO", "NAO"] and \
       Turno and Status:
        
        print(f"\n✅ SUCESSO: Aluno {Aluno}, seu CPF {CPF} foi validado!")
        break
    else:
        print(f"\n❌ ERRO: Dados inválidos! Tentativa {tentativa + 1} de 3.")
        print("-" * 40)
else:
    print("\n🚫 Bloqueado: muitas falhas. Procure o diretor de segurança.")
