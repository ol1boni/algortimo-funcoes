# 10. Crie função que valide login (user/senha)
def cadastrar_usuario():
    print ('\n')
    print ('ÁREA DE CADASTRO:')
    usuario_novo = input ('Crie um nome de usuário: ')
    senha_nova = input ('Crie uma senha: ')
    print ('Cadastro realizado!')
    return usuario_novo, senha_nova

def validar_login(usuario_correto, senha_correta, usuario_salvo, senha_salva):
    print ('Área de login:')
    if usuario_correto == usuario_salvo and senha_correta == senha_salva:
        return True
    else:
        return False
# Bloco principal de execução
if __name__ == "__main__":
    user_cadastrado, senha_cadastrada = cadastrar_usuario()
    while True:
        print ('\n')
        print('ÁREA DE LOGIN')

        user1 = input('Usuário: ')
        senha1 = input ('Senha: ')

        login_certo = validar_login(user1, senha1, user_cadastrado, senha_cadastrada)
        if login_certo:
            print ('Acesso liberado. Bem-vindo!')
            break
        else:
            print ('Acesso negado. Usuário ou senha incorretos!')