def checklist(lista, pd):
    for i, v in enumerate(lista):
        if i == len(lista)-1:
            return 1
        elif v < lista[i+1] and lista[i+1]-v < 4:
            continue
        elif pd == False:
            tmp_lista = lista[:i]+lista[i+1:]
            return checklist(tmp_lista, True)
        else:
            if  v < lista[i+1]:
                print(lista, v < lista[i+1],lista[i+1]-v < 4)
            return 0
        
def part2():
    file = open('input.txt','r')
    output = 0
    for row in file:
        row = [int(i) for i in row.split(" ")]
        tmp_output = checklist(row, False)
        if tmp_output == 0:
            row.reverse()
            tmp_output = checklist(row, False)
        output += tmp_output

    print(output)

part2()

#300,310 to low