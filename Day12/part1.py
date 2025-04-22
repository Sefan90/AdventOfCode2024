def getarea(x,y,map,lista):
  if y-1 >= 0 and map[y][x] == map[y-1][x] and str(y-1)+','+str(x) not in lista:
    lista.append(str(y-1)+','+str(x))
    lista = getarea(x,y-1,map,lista)
  if y+1 < len(map) and map[y][x] == map[y+1][x] and str(y+1)+','+str(x) not in lista:
    lista.append(str(y+1)+','+str(x))
    lista = getarea(x,y+1,map,lista)
  if x-1 >= 0 and map[y][x] == map[y][x-1] and str(y)+','+str(x-1) not in lista:
    lista.append(str(y)+','+str(x-1))
    lista = getarea(x-1,y,map,lista)
  if x+1 < len(map[0]) and map[y][x] == map[y][x+1] and str(y)+','+str(x+1) not in lista:
    lista.append(str(y)+','+str(x+1))
    lista = getarea(x+1,y,map,lista)
  return lista

def part1():
    map = [list(n) for n in open('input.txt','r').readlines()]
    print(map)
    dict = {}
    usedval = []

    for y in range(len(map)):
        for x in range(len(map[y])):
            if str(y)+','+str(x) not in usedval:
                dict[str(y)+','+str(x)] = []
                dict[str(y)+','+str(x)].append(str(y)+','+str(x))
                dict[str(y)+','+str(x)] = getarea(x,y,map,dict[str(y)+','+str(x)])
                usedval += dict[str(y)+','+str(x)]

    output = 0      
    for v in dict.values():
        v_output = 0
        for c in v:
            tmpc = c.split(',')
            tmp_output = 4
            if str(int(tmpc[0])+1)+','+str(tmpc[1]) in v:
                tmp_output -= 1
            if str(int(c[0])-1)+','+str(tmpc[1]) in v:
                tmp_output -= 1
            if str(tmpc[0])+','+str(int(tmpc[1])+1) in v:
                tmp_output -= 1
            if str(tmpc[0])+','+str(int(tmpc[1])-1) in v:
                tmp_output -= 1
            v_output += tmp_output
        output += v_output * len(v)
    print(output)

part1()

#3126437 high