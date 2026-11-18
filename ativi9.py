print ("--------------------------------SISTEMA DE TRAFEGO AEREO-----------------------------------------")

for tentativas in range(3):
 prefixo_aeronave = input("Digite o prefixo da aeronave: ").strip()
 companhia = input("Digite o nome da companhia: ").strip()
 codigo = input("Digite o codigo de voo: ").strip()
 altitude = input("Digite a altitude de cruzeiro: ").strip()
 velociade = input("Digite a velocidade: ").strip()
 pista = input("Digite a pista: ").strip()
 aeroporto = input("Digite o nome do aeroporto").strip ()
 codigo_transponder = input("Digite a matricula funcional do cargo ocupado: ").strip()
 email = input("Digite o E-mail da transportadora: ").strip()
 autorização = input("Digite o status do envio: ").strip().upper()

 if prefixo_aeronave.isalpha() and \
  companhia.isalpha() and \
  codigo.isalnum() and \
  altitude.isdigit() and \
  velociade.isdigit() and \
  pista.isdigit() and \
  aeroporto.isalpha() and \
   len(codigo_transponder) == 6 and \
       email.count("@") == 1 and \
       email.endswith("aircontrol.com") and \
       autorização == "PERMITIDO" :
          
          print(f"\nSUCESSO: Aeronave {prefixo_aeronave}, sistema {aeroporto} liberado!")
          break

 else:
      
  print(f"\nERRO: Dados invalidos! {tentativas + 1} de 3")
print("-" * 40)