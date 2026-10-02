def somar():
    numero1 = float(input("Digite um numero: "))
    numero2 = float(input("Digite outro numero: "))
    Resultado = numero1 + numero2
    print(f"Resultado: {Resultado}")

def subtrair ():
    numero1 = float(input("Digite um numero: "))
    numero2 = float(input("Digite outro numero: "))
    Resultado = numero1 - numero2
    print(f"Resultado: {Resultado}")

def multiplicar ():
    numero1 = float(input("Digite um numero: "))
    numero2 = float(input("Digite outro numero: "))
    Resultado = numero1 * numero2
    print(f"Resultado: {Resultado}")

def dividir ():
    numero1 = float(input("Digite um numero: "))
    numero2 = float(input("Digite outro numero: "))
    Resultado = numero1 / numero2
    print(f"Resultado: {Resultado}")
             
def Pares():
    numero = float(input("Digite um numero"))
    contador = 0
    numero_atual = 0 
 

    while contador < numero:
        print(numero_atual, end=" ")
        numero_atual += 2
        contador += 1

def Impares ():
    numero = float(input("Digite um numero:"))
    contador = 1 

    while contador <= numero:
        print(contador)
        contador = contador + 2    

def Somatorio ():
 print
        



    

 while True:
    print ("CALCULADORA")
    print ("1 - Adição")
    print ("2 - Subtração")
    print ("3 - Multiplicação")
    print ("4 - Divisão")
    print ("5 - Pares")
    print ("6 - Impares")
    print ("7 - Somatorio")
    print ("8 - Fatorial")
    print ("0 - Sair")

    opcao = input ("Escolha uma opção: ")
    
    if opcao == "1":
        somar()
       

    elif opcao == "2":
        subtrair()
        
    elif opcao == "3":
        multiplicar()
      
           
    elif opcao == "4":
        dividir()

    elif opcao == "5":
        Pares()    

    elif opcao == "6":
        Impares ()

    elif opcao == "0":
        print ("Saindo do sistema...")
        break
    else:
        print ("Opção inválida, tente novamente!!!")    