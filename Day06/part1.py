def move(guard, map):
    moves = [["^",-1,0],[">",0,1],["v",1,0],["<",0,-1]]
    for i, m in enumerate(moves):
        if map[guard[0]][guard[1]] == m[0]:
            if guard[0]+1 >= len(map) or guard[0]-1 < 0 or guard[1]+1 >= len(map[0]) or guard[1]-1 < 0:
                return guard, map
            elif map[guard[0]+m[1]][guard[1]+m[2]] in [".","X"]:
                map[guard[0]][guard[1]] = "X"
                map[guard[0]+m[1]][guard[1]+m[2]] = m[0]
                guard[0] += m[1]
                guard[1] += m[2]
            elif map[guard[0]+m[1]][guard[1]+m[2]] == "#":
                map[guard[0]][guard[1]] = moves[(i+1)%len(moves)][0]
    return guard, map

def part1():
    map = [c for c in [list(row.strip()) for row in open('input.txt','r')]]
    guard = [0,0]
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "^":
                guard = [y,x]
    while not(guard[0]+1 >= len(map) or guard[0]-1 < 0 or guard[1]+1 >= len(map[0]) or guard[1]-1 < 0):
        guard, map = move(guard,map)
    output = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] in ["X","^",">","v","<"]:
                output += 1
    print(output)
    
part1()