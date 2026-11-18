for tentativas in range(3):
   codigo = input("Digite o codigo (deve conter 6 caracteristicas):").strip()
   destino = input("Digite o destino (deve conter 3 letras):").strip()

   if len(codigo) == 6 and len(destino) >3:
      print(f"Digite seu codigo e {codigo} Seu destino e {destino}")
      break
   else:
      print("Seu codigo esta incorreto. tente novamente!")
else:
   print("Seu destino esta incorreto. tente novamente!")