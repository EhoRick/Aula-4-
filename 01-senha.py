nome_digitado = input ("Digite o nome:")
senha_digitada = input ("Digite sua senha:")
senha_cadastrada = "123"
nome_cadastrado = "Rick"

while senha_digitada != senha_cadastrada and nome_digitado != nome_cadastrado or nome_cadastrado != senha_cadastrada:
    print ("Usuario e senha incorretos tente novamente.")
    senha_digitada = input("Digite seu usuario:")

print (f"{nome_cadastrado} Bem-vindo ao Sistema...")    


