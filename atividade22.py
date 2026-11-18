print("---------- voo ----------")

for tentativa in range(3):
   voo = input("Digite o codigo do voo: ").strip()
   assento = input("digite seu assento:").strip ()

   if len(voo) == 4 and len(assento) == 3:
    print(f"Seu voo esta correto {voo} e assento {assento} aceitos")
   break
else:
 print("acesso negado")
print("-" * 30)