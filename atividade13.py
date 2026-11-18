passageiro = ["Bruno", "Carla", "Diego", "pedro", "mateus","kaio", "daniel","ana","maria","natanael"]

for pessoa in passageiro:

    peso = int(input(f"Digite o peso da mala {pessoa}: "))

    if peso > 23:
         print(f"Bagagem liberada: {pessoa}.")
    else:
        print(f"Deve pagar taxa extra: {pessoa}.")