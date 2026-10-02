nome = input ("Digite seu nome:")
nota =  int (input ("Digite sua nota:"))
outra_nota = str (input ("Deseja digitar outra nota?:"))
quantidade = 0
soma_notas = nota


while outra_nota == "sim":
    nota = int (input ("Digite sua outra nota:"))
    soma_notas = soma_notas + nota
    quantidade = quantidade + 1 
    outra_nota = input ("Deseja digitar outra nota?:") 


media = soma_notas / quantidade

if media >= 6:
    print (f"{media} Aprovado!")

elif media == 5:
    print (f"{media} Recuperação!")

else:
    print (f"{media} Reprovado!")



    





