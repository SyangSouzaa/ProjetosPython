# Questão 2 - Login

print("=== FAÇA SEU LOGIN ===")

login = input("Login: ")
senha = input("Senha: ")

if (login == "scott" and senha == "tiger") or \
   (login == "walt" and senha == "disney") or \
   (login == "spock" and senha == "ncc1701"):
    print("Autenticado com sucesso")
else:
    print("Usuário ou senha inválidos")