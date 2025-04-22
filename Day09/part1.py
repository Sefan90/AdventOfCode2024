def part1():
    lista = []
    output = 0
    for row in open('input.txt','r'):
        counter = 0
        for i, c in enumerate(row.strip()):
            if i%2 == 0:
                for j in range(int(c)):
                    lista.append(counter)
                counter += 1
            else:
                for j in range(int(c)):
                    lista.append(".")

    for i, c in enumerate(lista):
        while lista[-1] == ".":
            lista = lista[:-1]
        if c == "." and i < len(lista):
            lista[i] = lista[-1]
            lista = lista[:-1]
        elif i >= len(lista):
            lista = lista[:i]
    print(lista)
    for i, c in enumerate(lista):
        output += i*c
    print(output)
part1()

