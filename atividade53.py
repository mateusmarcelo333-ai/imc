print("--- Sistema de auditoria completo ---")

for tentativa in range(3):
    Projeto = input("Digite o nome do seu projeto: ")
    Código = input("Digite o seu codigo de acesso: ")
    Engenheiro = input("Digite o seu nivel de engenharia: ")
    Crea = input("Digite o seu Crea: ")
    Setor = input("Digite o seu setor: ")
    Orçamento = input("Digite o seu orçamento: ")
    Data_inicial = input("Digite sua data DD/MM/AAAA: ")
    Data_fim = input("Digite sua data de fim DD/MM/AAAA: ")
    Cidade = input("Digite a sua cidade: ")
    UF = input("Digite a sua UF: ")
    Email_resp = input("Digite o seu Email_resp: ")
    Cliente = input("Digite o seu Cliente: ")
    CNPJ = input("Digite o seu CNPJ 14 NUM: ")
    Prioridade = input("Digite a sua Prioridade: ")
    Status = input("Digite o seu Status: ")

    if  Projeto.isalnum() and \
        Setor.isalnum() and \
        UF.isalnum() and \
        Status.isalnum() and \
        Código.isalnum() and \
        Engenheiro.isalpha() and \
        Cidade.isalpha() and \
        Crea.isdigit() and \
        Orçamento.isdigit() and \
        CNPJ.isdigit() and \
        Email_resp.count("@") == 1 and Email_resp.endswith(".com") and \
        Data_inicial.count("/") == 2 and \
        Data_fim.count("/") == 2 and \
        Status == "Aprovado":
    
        print(f"\nSUCESSO Status {Status}, seu relatorio {Projeto} foi enviado!")
        break
    else:
        print(f"\nERRO: Dados invalidos! Tentativa {tentativa + 1} de 3.")
        print("-" * 40)
else:
    print("\nBloqueado: muitas falhas. Procure o diretor de segurança.")