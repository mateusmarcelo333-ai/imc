print("--- MANIFESTO DE CARGA ---")
navio = input("Navio: ").strip()
capitao = input("Capitão: ").strip()
origem = input("Origem: ").strip()
destino = input("Destino: ").strip().upper()
carga = input("Carga: ").strip()
peso = input("Peso (ton): ").strip()
containers = input("Containers: ").strip()
valor = input("Valor: ").strip()
seguro = input("Seguro: ").strip()
porto = input("Porto: ").strip()
empresa = input("Empresa: ").strip().upper()
licenca = input("Licença (8 num): ").strip()
rota = input("Rota: ").strip().upper()
combustivel = input("Combustível: ").strip()
chegada = input("Chegada: ").strip()

if capitao.isalpha() and \
   origem.isalpha() and \
   licenca.isdigit() and peso.isdigit() and \
   destino == "EUROPA" and \
   empresa != "FANTASMA" and \
   rota == "SUL":

    print(" Manifesto aprovado!")
else:
    print(" Manifesto recusado: Dados inconsistentes.")