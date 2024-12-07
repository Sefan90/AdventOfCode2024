def checklist(lista):
    for i, v in enumerate(lista):
        if i == len(lista)-1:
            return 1
        elif int(v) < int(lista[i+1]) and int(lista[i+1])-int(v) < 4:
            continue
        else:
            return 0
        
def part1():
    file = open('input.txt','r')
    output = 0
    for row in file:
        row = row.split(" ")
        if int(row[0]) < int(row[1]):
            output += checklist(row)
        else:
            row.reverse()
            output += checklist(row)

    print(output)

part1()