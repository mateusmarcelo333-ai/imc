crianças = ["Bruno", "Carla", "Diego"]

for pessoa in crianças:

    altura = int(input(f"Digite a altura de {pessoa} em centímetros: "))

    if altura > 140:
        print(f"Pode subir: {pessoa}.")
    else:
        print(f"Não pode subir: {pessoa}.")