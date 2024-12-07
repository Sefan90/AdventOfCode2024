def findchars(y,x):
    if y-1 > -1 and y-1 < len(map) and x-1 > -1 and x-1 < len(map[y]) and map[y-1][x-1] == 'M':
        if y+1 > -1 and y+1 < len(map) and x+1 > -1 and x+1 < len(map[y]) and map[y+1][x+1] == 'S':
            if y+1 > -1 and y+1 < len(map) and x-1 > -1 and x-1 < len(map[y]) and map[y+1][x-1] == 'S':
                if y-1 > -1 and y-1 < len(map) and x+1 > -1 and x+1 < len(map[y]) and map[y-1][x+1] == 'M':
                    return 1
            elif y+1 > -1 and y+1 < len(map) and x-1 > -1 and x-1 < len(map[y]) and map[y+1][x-1] == 'M':
                if y-1 > -1 and y-1 < len(map) and x+1 > -1 and x+1 < len(map[y]) and map[y-1][x+1] == 'S':
                    return 1
    elif y+1 > -1 and y+1 < len(map) and x+1 > -1 and x+1 < len(map[y]) and map[y+1][x+1] == 'M':
        if y-1 > -1 and y-1 < len(map) and x-1 > -1 and x-1 < len(map[y]) and map[y-1][x-1] == 'S':
            if y+1 > -1 and y+1 < len(map) and x-1 > -1 and x-1 < len(map[y]) and map[y+1][x-1] == 'S':
                if y-1 > -1 and y-1 < len(map) and x+1 > -1 and x+1 < len(map[y]) and map[y-1][x+1] == 'M':
                    return 1
            elif y+1 > -1 and y+1 < len(map) and x-1 > -1 and x-1 < len(map[y]) and map[y+1][x-1] == 'M':
                if y-1 > -1 and y-1 < len(map) and x+1 > -1 and x+1 < len(map[y]) and map[y-1][x+1] == 'S':
                    return 1
    return 0



def part2():
    output = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 'A':
                output += findchars(y,x)
    print(output)

map = [list(row.strip()) for row in open('input.txt','r')]
part2()