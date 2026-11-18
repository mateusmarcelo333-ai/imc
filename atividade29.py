print("----------------------------Prontuario Medico-----------------------------")
paciente = input("Digite o nome do paciente: ").strip()
medico = input("Digite seu pais ( Deve conter mais de 4 letras): ").strip()
hospital = input("Digite o nome do Hospital (Deve conter exatamente 4 caracteres) :")
crm = input("Digite o crm (Deve conter exatamente 5 letras) :")
ala = input("Digite a ala medica (deve conter exatamente 2 letras) :")
sintomas = input("Digite o seu sintomas (Não pode ser nada) :")

if len(paciente) >4 and len(medico) >4 and len(hospital) > 4 and len(crm) == 5 and len(ala) == 2 and len(sintomas) !="Nada":
    print(f"O nome do hospede e {paciente}, Seu pais e {medico}, Seu passaporte e {crm}, a data e {ala}, seu turno e {sintomas}")
else:
    print("nome do paciente, medico, hospital, crm, ala ou sintomas esta incorreto(a)!. Tente novamente mais tarde")