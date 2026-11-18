print ("--------------------------------Medico hospitalar-----------------------------------------")

for tentativas in range(5):
    Nome_do_paciente = input("Digite o nome do Paciente: ").strip()
    Especialidade_Medica = input("Digite a sua Especialidade medica: ").strip()
    Numero_do_prontuario = input("Digite o Numero do prontuario: ").strip().upper()
    CRM_do_medico = input("Digite o CRM do medico: ").strip()
    Codigo_do_Convenio= input("Digite o Codigo do convencio: ").strip()
    Batimentos_cardiacos = input("Digite o seu Batimento cardioco: ").strip().lower()
    Temperatura_Corporal = input("Digite a sua Temperatura Corporal: ").strip()
    Sala_de_atendimento = input("Digite a sala de atedimento: ").strip().upper()
    Email_do_hospital = input("Digite o Email do hospital: ").strip()
    Status_da_Triagem = input("Digite Urgencia: ").strip().upper()

    if Nome_do_paciente.isalpha() and \
       Especialidade_Medica.isalpha() and \
       Numero_do_prontuario.isdigit() and \
       Batimentos_cardiacos.isdigit() and \
       CRM_do_medico.isalnum() and \
       Codigo_do_Convenio.isalnum() and \
       len(CRM_do_medico) ==7 and \
       Email_do_hospital.count ("@") == 1 and Email_do_hospital.endswith (".med.br") and \
       Status_da_Triagem == "Urgente":

       print(f"\nSUCESSO:  {Nome_do_paciente},  {Numero_do_prontuario} liberado!")
       break
    else:
         print(f"\nERRO: Dados invalidos! {tentativas + 1} de 5")
         print("-" * 40)
else:
     print("Acesso negado")