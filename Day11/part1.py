import math

def part1():
    lista = [int(n) for n in open('input.txt','r').readline().split(" ")]
    for a in range(25):
        newlista = []
        for i in range(len(lista)):
            if lista[i] == 0:
                newlista.append(1)
            elif int(math.log10(lista[i])+1)%2 == 0:
                newlista.append(int(str(lista[i])[:int(math.log10(lista[i])+1)//2]))
                newlista.append(int(str(lista[i])[int(math.log10(lista[i])+1)//2:]))
            else:
                newlista.append(lista[i]*2024)
        lista = newlista

    print(len(lista))

part1()

