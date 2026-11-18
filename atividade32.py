curso = input("Digite qual e o curso (Deve conter apenas letras):").strip()
nome = input("nome").strip()
matricula = input("Digite sua matricula (Deve conter exatamente 6 numeros)").strip
ano = input("Digite o ano (Deve conter 4 digitos numericos)").strip()
Campus = input("Digite seu campus (deve ser exatamente igual a central)").strip()
senha = input("Digite sua senha (não pode ser 12345)").strip()

if curso.isalpha() and \
   nome.isalpha() and \
   len(matricula) == 6 and matricula.isalpha() and \
   len(ano) == 4 and ano.isdigit() and \
   senha.isdigit != "1234" and \
   Campus.isalpha =="central":
    
    print("Aluno matriculado com sucesso! Bem-Vindo")
else:
    print("erro: verifique as esta tudo correto")