def part1():
    inputpages = False
    leftrules = []
    rightrules = []
    pages = []
    for row in open('input.txt','r'):
        if row == "\n":
            inputpages = True
        elif inputpages:
            pages.append(row.strip().split(","))
        else:
            leftrules.append(row.strip().split("|")[0])
            rightrules.append(row.strip().split("|")[1])

    output_pages = []
    for row in pages:
        correctPage = True
        for p in row:
            for i,l in enumerate(leftrules): 
                if p == l:
                    try:
                        #print(row.index(p))
                        #print(row.index(rightrules[i]))
                        if row.index(rightrules[i]) < row.index(p):
                            #print(p,rightrules[i],row.index(rightrules[i]), row.index(p))
                            correctPage = False
                    except:
                        continue
        #print(row, correctPage)
        if correctPage:
            output_pages.append(row)
    output = 0
    for op in output_pages:
        output += int(op[int((len(op) - 1)/2)])
    print(output)
part1()