frutas = ['laranja', 'maça',  'uva']
frutas = []

letras = list("python")

num = list(range(20))

carro = ['Ferrari', 'F8', 4200000, 2020, 'BH']

# a lista é uma sequencia, com indices
# indices negativos começam com o ultimo indice

frutas = [-1] # uva

# listas podem armazenar outros objetos, pode ter listas armazenadas em outras listas

matriz = [
    [1, 'a', 3]
    ['b', 1, 5]
    [6, 5, 'c']
]

matriz[0][0]

# fatiamento, uma forma de acessar um conjunto de elementos

lista = ['p', 'y', 't', 'h', 'o', 'n']

lista[2:]
lista[:2] # ['p', 'y']
lista[1:3] # inicial e final
lista[0:3:2]
lista[::-1] # inverte a lista

# iterar listas
carros = ['gol', 'celta', 'caminhão']
for carro in carros:
    print(carro)


# compreensão de listas 
numeros = [1, 2, 4, 8, 6, 5]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

pares2 = [numero for numero in numeros if numero % 2 == 0]        

quadrado = [numero ** 2 for numero in numeros]

# [].append
lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)  # [1, "Python", [40, 30, 20]]

# []. clear
lista = [1, "Python", [40, 30, 20]]

print(lista)  # [1, "Python", [40, 30, 20]]

lista.clear()

print(lista)  # []

# [].copy
lista = [1, "Python", [40, 30, 20]]

lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]

# [].count
cores = ["vermelho", "azul", "verde", "azul"]

print(cores.count("vermelho"))  # 1
print(cores.count("azul"))  # 2
print(cores.count("verde"))  # 1

# [].extend - adicionar novos elementos na lista - para extender
linguagens = ["python", "js", "c"]

print(linguagens)  # ["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens)  # ["python", "js", "c", "java", "csharp"]

# [].index
linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  # 0

# [].pop - remove elemento por indice
linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.pop())  # csharp
print(linguagens.pop())  # java
print(linguagens.pop())  # c
print(linguagens.pop(0))  # python

# [].remove - remove elemento por referencia
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.remove("c")

print(linguagens)  # ["python", "js", "java", "csharp"]

# [].reverse - inverter a lista
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.reverse()

print(linguagens)  # ["csharp", "java", "c", "js", "python"]

# [].sort - ordenar a lista 
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens)

# sorted - ordernar iteraveis
linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]
# 
