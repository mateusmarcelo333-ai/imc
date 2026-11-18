# clima
temperatura = float(input("Digite a temperatura atual em °C: "))

if temperatura > 30:
    print("Está calor! Use roupas leves.")
elif temperatura >= 20:
    print("Clima agradável, use camiseta.")
elif temperatura >= 10:
    print("O tempo esfriou, leve um casaco leve.")
else:
    print("Está muito frio, use roupas pesadas.")