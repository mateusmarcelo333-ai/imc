print ("--------------------------------SISTEMA DE AUDITORIA-----------------------------------------")

for tentativas in range(3):
 nome_funcionario = input("Digite o nome do funcionario: ").strip()
 departamneto = input("Digite o departamento: ").strip()
 cargo = input("Digite o cargo: ").strip()
 salario = input("Digite o salrio base: ").strip()
 horas = input("Digite as horas trabalhadas: ").strip()
 codigo = input("Digite o codigo do banco: ").strip()
 matricula = input("Digite a matricula funcional do cargo ocupado: ").strip()
 email = input("Digite o E-mail da transportadora: ").strip()
 parecer = input("Digite o status do envio: ").strip().upper()

 if nome_funcionario.isalpha() and \
     departamneto.isalpha() and \
     cargo.isalnum() and \
     salario.isdigit() and \
     horas.isdigit() and \
     codigo.isdigit() and \
     len(matricula) == 6 and \
     email.count("@") == 1 and \
     email.endswith(".log.br") and \
     parecer == "VALIDADO":

      print(f"\nSUCESSO: funcionario {nome_funcionario}, sistema {departamneto} liberado!")
      break

 else:

  print(f"\nERRO: Dados invalidos! {tentativas + 1} de 3")
  print("-" * 40)
  
  print("\nBLOQUEIO: limite de 3 tentativas excedido. Procure o agente de TI")