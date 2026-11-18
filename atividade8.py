# Criamos uma lista de nomes para o programa percorrer 
convidados = ["Ana", "Bruno", "Carla"]

# O FOR funciona como um laço que pega um nome or vez da lista
for pessoa in convidados:

    # O INPUT para programar e esperar o usuario digitar a idade
    # O INT transforma o que foi digitado em um numero inteiro
    idade = int(input("qual a idade de "+ pessoa + "?"))

    # O IF faz a pergunta: a idade é maior ou igual a 18?
    if idade >= 18:
    #se for verdade, o python executa esta linha:
     print(pessoa, "e maior de idade. Acesso liberado!")

    # O ELSE é o "caso contrario"(se a pergunta do IF for falsa)
else:
    #se for MENOR de 18, python executa esta linha:
    print(pessoa, "é menor de idade. Acesso negado!")