print("--- Sistema de auditoria completo---")

for tentativa in range(3):
    # Coletando e tratando os dados
    # Removi o traço antes de checar o .isalnem() para a logica funcionar
    codigo = input("cód. relatorio (ex: re101):")
    data = input("Data (DD/MM/AAAA):")
    email = input("E-mail do auditor:")
    id_auditor = input("ID numero do auditor:")
    Status = input("Status (Digite Aprovado):")

    # Explicaçao da logica:
    # o .isalnum() verifiqu se o codigo contem apenas letras numeros (sem simbolos ou espaços).
    # o .count("/") == 2 verifica se existem exatamente DUAS barras na data.
    # o .count("@") == 1 verifica se existe exatamente um arroba no e-mail.
    # o .endswith(".com") garante que o e-mail termine corretamente.
    # o .isdigit() garante que o ID do auditor seja apenas numeros.
    if codigo.isalnum() and \
       data.count("/") == 2 and \
       email.count("@") == 1 and email.endswith(".com") and \
       id_auditor.isdigit() and \
       Status == "APROVADO":
        
        print(f"\n✅ SUCESSO Auditor {id_auditor}, seu relatorio {codigo} foi enviado!")
        break
    else:
        #Exibe o numero da tentativa amigavel (1, 2 ou 3)
        print(f"\n❌ ERRO: Dados invalidos! tentativas {tentativa + 1} de 3.")
        print("-"* 40)
else:
    print("f\n🚫 Bloqueado: muitas falhas. procura o diretor de segurança.")

    #📝 Legendas tecnica: o que cada funçao faz neste codigo?  