
tentativas = [
    ("joao", "123"),
    ("admin", "senha_errada"),
    ("admin", "admin123"),
    ("maria", "abc"),
    ("admin", "9876")
]
usuario_correto = "admin"
senha_correta = "admin123"

for usuario, senha in tentativas:
    if usuario == usuario_correto and senha == senha_correta:
        print(f"Usuário {usuario}: Acesso liberado")
    else:
        print(f"Usuário {usuario}: Acesso negado (Usuário ou senha incorretos)")