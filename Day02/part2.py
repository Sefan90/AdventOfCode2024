def checklist(lista, pd, next):
    for i, v in enumerate(lista):
        if i == len(lista)-1:
            return 1
        elif v < lista[i+1] and lista[i+1]-v < 4 and lista[i+1]-v > 0 and (next == 0 or next == 1):
            next = 1
            continue
        elif v > lista[i+1] and v-lista[i+1] < 4 and v-lista[i+1] > 0 and (next == 0 or next == -1):
            next = -1
            continue
        elif pd == False:
            tmp_lista = lista[:i]+lista[i+1:]
            tmp_ret = checklist(tmp_lista, True, next)
            if tmp_ret == 0 and i != 0:
                tmp_lista = lista[:i-1]+lista[i:]
                tmp_ret = checklist(tmp_lista, True, next)
            return tmp_ret
        else:
            return 0
        
def part2():
    file = open('input.txt','r')
    output = 0
    for row in file:
        row = [int(i) for i in row.split(" ")]
        tmp_output = checklist(row, False,0)
        output += tmp_output

    print(output)

part2()

#300,310 to low
#320 wrong
#315 wrong
#497 wrong

#315