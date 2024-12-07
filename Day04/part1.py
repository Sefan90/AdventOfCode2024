def findchar(y,x,c,sy,sx):
    noOfWords = 0
    if c >= len(word):
        return 1
    elif sy == 0 and sx == 0:
        for iy in range(-1,2):
            for ix in range(-1,2):
                if y+iy > -1 and y+iy < len(map) and x+ix > -1 and x+ix < len(map[y]) and map[y+iy][x+ix] == word[c]:
                    noOfWords += findchar(y+iy,x+ix,c+1,iy,ix)
    elif y+sy > -1 and y+sy < len(map) and x+sx > -1 and x+sx < len(map[y]) and map[y+sy][x+sx] == word[c]:
        noOfWords += findchar(y+sy,x+sx,c+1,sy,sx)

    return noOfWords

def part1():
    output = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 'X':
                output += findchar(y,x,1,0,0)
    print(output)

word = 'XMAS'
map = [list(row.strip()) for row in open('input.txt','r')]
part1()