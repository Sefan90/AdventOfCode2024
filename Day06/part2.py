def loop(pages,leftrules,rightrules):
    output_pages = []
    for row in pages:
        for p in row:
            for i,l in enumerate(leftrules): 
                if p == l:
                    try:
                        if row.index(rightrules[i]) < row.index(p):
                            tmppage = row.index(rightrules[i])
                            row[row.index(p)] = rightrules[i] 
                            row[tmppage] = p
                            print(row)
                    except:
                        continue
        output_pages.append(row)
    if pages == output_pages:
        return pages
    else:
        return loop(output_pages,leftrules,rightrules)
    
def part2():
    inputpages = False
    leftrules = []
    rightrules = []
    pages = []
    for row in open('testinput.txt','r'):
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
                        if row.index(rightrules[i]) < row.index(p):
                            tmppage = row.index(rightrules[i])
                            row[row.index(p)] = rightrules[i] 
                            row[tmppage] = p
                            correctPage = False
                            print(row)
                    except:
                        continue
        if correctPage == False:
            output_pages.append(row)
    
    print(len(output_pages))
    output_pages = loop(output_pages,leftrules,rightrules)
    print(len(output_pages))
    output = 0
    for op in output_pages:
        output += int(op[int((len(op) - 1)/2)])
    print(output)
part2()

#low 4628 
#low 4931