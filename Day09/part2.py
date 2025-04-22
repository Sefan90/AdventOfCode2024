def part2():
    lista = ""
    output = 0
    maxno = 0 
    for row in open('testinput.txt','r'):
        counter = 0
        for i, c in enumerate(row.strip()):
            if i%2 == 0:
                lista += ' '+str(counter)*int(c)
                if maxno < int(str(counter)*int(c)):
                    maxno = int(str(counter)*int(c))
                counter += 1
            else:
                lista += ' '+"."*int(c)
    print(lista)
    for i in range(maxno,0,-1):
        lastfile = ' '+str(i)+' '
        filecount = lista.count(lastfile)
        if lastfile == ".":
            continue
        elif filecount > 0:
            index = lista.find("."*filecount)
            fileindex = lista.find(lastfile*filecount)
            if index > -1 and fileindex > -1 and index < fileindex: 
                lista = lista[:index]+lastfile*filecount+lista[index+filecount:fileindex]+"."*filecount+lista[fileindex+filecount:]
                print(lista+"\n")
                
    print(lista)
    for i, c in enumerate(lista.replace(" ","")):
        if c != ".":
            output += i*int(c)
    print(output)
part2()

#001199211777.44.333....5555.6666.....8888..
#00992111777.44.333....5555.6666.....8888..