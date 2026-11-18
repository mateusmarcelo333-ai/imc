print ("--------------------------------Repositorio Git-----------------------------------------")

for tentativas in range(5):
    Nome_do_Desenvolvedor = input("Digite o nome do Desenvolvedor: ").strip()
    Nickname = input("Digite a sua Especialidade medica: ").strip()
    Nome_do_repositor = input("Digite o Numero do prontuario: ").strip().upper()
    ID = input("Digite o CRM do medico: ").strip()
    Quantidade= input("Digite o Codigo do convencio: ").strip()
    Branch = input("Digite o seu Batimento cardioco: ").strip().lower()
    Linguagem = input("Digite a sua Temperatura Corporal: ").strip()
    Chave = input("Digite a sala de atedimento: ").strip().upper()
    Email_institucional = input("Digite o Email do hospital: ").strip()
    Status_da_Deploy = input("Digite (Sucesso): ").strip().upper()

    if     Nickname.isalnum() and \
           Nome_do_repositor.isalnum() and \
           ID.isalnum() and \
           Quantidade.isdigit() and \
           Nome_do_Desenvolvedor.isalpha and \
           Linguagem.isalpha and \
           Email_institucional.count ("@") == 1 and Email_institucional.endswith (".edu.br") and \
           len(Chave) ==12 and \
           Status_da_Deploy == "Sucesso":
    
           print(f"\nSUCESSO:  {Nome_do_repositor},  {Quantidade} liberado!")
           break
    else:
             print(f"\nERRO: Dados invalidos! {tentativas + 1} de 5")
             print("-" * 40)
else:
         print("Acesso negado")