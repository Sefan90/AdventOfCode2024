def part2():
    antennas = {}
    map = [list(row.strip()) for row in open('input.txt','r')]
    maxdist = max(len(map),len(map[0]))
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] != ".":
                if map[y][x] in antennas.keys():
                    antennas[map[y][x]].append([y,x])
                else:
                    antennas[map[y][x]] = []
                    antennas[map[y][x]].append([y,x])
    antinodes = []
    for row in antennas.values():
        for i in row:
            for j in row:
                if i != j:
                    for d in range(maxdist):
                        newnode = False
                        if j[0]+(j[0]-i[0])*d < len(map) and j[1]+(j[1]-i[1])*d < len(map[0]) and j[0]+(j[0]-i[0])*d >= 0 and j[1]+(j[1]-i[1])*d >= 0:
                            antinodes.append(str(j[0]+(j[0]-i[0])*d)+"."+str(j[1]+(j[1]-i[1])*d))
                            newnode = True
                        if i[0]+(i[0]-j[0])*d < len(map) and i[1]+(i[1]-j[1])*d < len(map[0]) and i[0]+(i[0]-j[0])*d >= 0 and i[1]+(i[1]-j[1])*d >= 0:
                            antinodes.append(str(i[0]+(i[0]-j[0])*d)+"."+str(i[1]+(i[1]-j[1])*d))
                            newnode = True
                        if newnode == False:
                            break
    antinodes = list(set(antinodes))
    print(len(antinodes))

part2()