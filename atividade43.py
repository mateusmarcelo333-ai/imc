print("---PRONTUARIO MEDICO DA UTI---")

for tentativa in range(3):

    paciente = input("Digite o nome do pasciente:  ").strip()
    medico = input("Digite o nome do medico: ").strip()
    leito = input("Digite o leito (Apenas numeros): ").strip()
    crm = input("Digite seu crm (Deve conter apenas numeros): ").strip()
    batimentos = input("Digite os batimentos (Deve conter apenas numeros): ").strip()
    tipo = input("Digite o seu tipo sanguineo (Deve ser O+ ou similar) : ").strip().upper()
    alergia = input("Digite sua alergia (Deve pode ser NADA) : ").strip().upper()

    if paciente.isalpha() and paciente.isalpha() and \
       medico.isalpha() and \
       leito.isdigit() and \
       crm.isdigit() and \
       batimentos.isdigit() and \
       len(tipo) and tipo.isalpha() == "O+" and \
       len(alergia) and alergia.isdigit() != "NADA":

        print(f"Acesso liberado! Bem-vindo ao sistema, {paciente}.")
        break

else:
    print("SISTEMA BLOQUEADO. Alerta de intrusão enviado à segurança.")