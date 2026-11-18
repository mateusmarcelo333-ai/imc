# O Semáforo Inteligente
cor = input("Qual a cor do semáforo? (verde / amarelo / vermelho): ")

if cor == "verde":
    print("Ação: ACELERE. O caminho está livre.")
elif cor == "amarelo":
    print("Ação: ATENÇÃO. Reduza a velocidade e prepare-se para parar.")
elif cor == "vermelho":
    print("Ação: PARE imediamente.")
else:
    print("ERRO: cor inválida.")