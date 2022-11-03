#Definição para cálculo de Fibonacci

def fibonacci(x):

    if x <= 1:
        return 1
    else:
        return fibonacci(x-1)+fibonacci(x-2)

#Definição para cálculo de Fatorial 

def fatorial(x):

    if x == 1:
        return x
    else:
        return x*fatorial(x-1)

#Aqui, será lido o arquivo
file = open('rascunho.dat','r')   
dados = file.readlines()       

#Aqui, será feito um print dos dados do arquivo em questão
print(dados)

#Aqui, será feito um print dos dados da nova lista
lista = [numero.strip().split() for numero in dados]

with open('resultado.dat','w') as output:

    n = 1
    for item in lista:
        z, y= item
        a = fibonacci(int(z))
        b = fatorial(int(y))
        output.write(f"Linha {n}: Fib{z}={a} Fact{y}={b}\n")
        n+=1