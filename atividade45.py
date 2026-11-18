print("--- PRONTUÁRIO MÉDICO DE CIRURGIA ROBÓTICA ---")

paciente = input("Paciente: ").strip()
cpf = input("CPF (11 num): ").strip()
idade = input("Idade: ").strip()
peso = input("Peso: ").strip()
altura = input("Altura: ").strip()
medico = input("Médico: ").strip()
crm = input("CRM (6 num): ").strip()
robo = input("Robô: ").strip().upper()
sala = input("Sala: ").strip()
hospital = input("Hospital: ").strip().upper()
tipo_sangue = input("Tipo Sangue (2 ou 3 carac): ").strip()
alergia = input("Alergia: ").strip()
anestesia = input("Anestesia: ").strip()
batimentos = input("Batimentos: ").strip()
oxigenio = input("Oxigênio: ").strip()

if paciente.isalpha() and medico.isalpha() and \
   crm.isdigit() and cpf.isdigit() and \
   robo == "DA_VINCI" and \
   hospital != "TESTE" and \
   (len(tipo_sangue) == 2 or len(tipo_sangue) == 3) and \
   batimentos.isdigit() and oxigenio.isdigit():
    
    print("\n Prontuário validado com sucesso!")
else:
    print("\n Erro: Um ou mais campos não atendem às regras de segurança.")