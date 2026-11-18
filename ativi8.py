print ("--------------------------------Autoatendimento Bancario-----------------------------------------")

for tentativas in range(5):
    Nome_do_correntista = input("Digite o nome do correntista: ").strip()
    Tipo_de_conta = input("Digite o seu tipo de conta: ").strip()
    Número_da_Agencia= input("Digite o numero da agencia: ").strip().upper()
    Número_do_cartão= input("Digite o numero do cartao: ").strip()
    Valor_do_saque = input("Digite o valor do saque: ").strip()
    Pin_de_segurança = input("DIgite o pin de segurança")
    Codigo_do_terminal = input("Digite o terminal: ").strip().lower()
    cidade_do_caixa = input("Digite a cidade do caixa: ").strip()
    Email = input("Digite o email da empresa: ").strip().upper()
    Operação_final = input("(CONCLUIDO)")

    if Número_da_Agencia.isdigit() and\
       Número_do_cartão.isdigit() and\
       Valor_do_saque.isdigit() and\
       Pin_de_segurança.isdigit() and\
       len(Pin_de_segurança) ==4 and\
       Nome_do_correntista.isalpha and \
       cidade_do_caixa.isalpha and \
       Codigo_do_terminal.isalnum and \
       Email.count ("@") == 1 and Email.endswith (".bank.com") and \
       Operação_final == "CONCLUIDO":

        print(f"\nSUCESSO:  {Nome_do_correntista},  {Número_da_Agencia} liberado!")
        break
    else:
        print(f"\nERRO: Dados invalidos! {tentativas + 1} de 5")
        print("-" * 40)
else:
    print("Acesso negado")