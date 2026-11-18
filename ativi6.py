print ("--------------------------------Despacho de cargas-----------------------------------------")

for tentativas in range(5):
    Nome_do_motorista = input("Digite o nome do motorista: ").strip()
    cidade = input("Digite da cidade: ").strip()
    Placa = input("Digite o Numero da placa: ").strip().upper()
    Codigo= input("Digite o codigo: ").strip()
    peso = input("Digite o peso: ").strip()
    Numero_da_nota_fiscal = input("Digite o numero da nota fiscal")
    Tipo_de_Trasporte = input("Digite o seu tipo de transporte: ").strip().lower()
    Email_da_trasportadora = input("Digite o Email da transportadora: ").strip()
    Status_da_Deploy = input("Digite (Sucesso): ").strip().upper()
    CEP_da_entrega = input("Digite o CEP:")
    Status_do_envio = input("AUTORIZADO")

    if Nome_do_motorista.isalpha() and \
       cidade.isalpha() and \
       Tipo_de_Trasporte.isalpha() and \
       Placa.isalnum() and \
       Codigo.isalnum() and \
       peso.isdigit() and \
       Numero_da_nota_fiscal.isdigit() and \
        len(CEP_da_entrega) ==8 and \
       Email_da_trasportadora.count ("@") == 1 and Email_da_trasportadora.endswith (".log.br") and \
        Status_da_Deploy == "AUTORIZADO":
           
        print(f"\nSUCESSO:  {Nome_do_motorista},  {Placa} liberado!")
        break
    else:
         print(f"\nERRO: Dados invalidos! {tentativas + 1} de 5")
         print("-" * 40)
else:
    print("Acesso negado")