def solvepath(map,by,bx,y,x,nines):
    if map[y][x] == 9:
        nines[str(by)+"."+str(bx)].append(str(y)+"."+str(x))
        return 0
    if y+1 < len(map) and map[y+1][x] == map[y][x]+1:
        solvepath(map,by,bx,y+1,x,nines)
    if y-1 > -1 and map[y-1][x] == map[y][x]+1:
        solvepath(map,by,bx,y-1,x,nines)
    if x+1 < len(map[0]) and map[y][x+1] == map[y][x]+1:
        solvepath(map,by,bx,y,x+1,nines)
    if x-1 > -1 and map[y][x-1] == map[y][x]+1:
        solvepath(map,by,bx,y,x-1,nines)
    return 0

def part1():
    map = [[int(n) for n in row.strip()] for row in open('input.txt','r')]
    nines = {}
    output = 0

    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 0:
                nines[str(y)+"."+str(x)] = []
                solvepath(map,y,x,y,x,nines)
    
    for key in nines.keys():
        nines[key] = list(set(nines[key]))
        output += len(nines[key])
    print(output)

part1()

