def solve(res,values,i,calc):
    if calc == res and (i == len(values) or i == len(values)+1):
        return True
    elif i < len(values):
        tmpret = solve(res,values,i+1,calc*values[i])
        if tmpret == False:
            tmpret = solve(res,values,i+1,calc+values[i])
            if tmpret == False:
                tmpret = solve(res,values,i+1,int(str(calc)+str(values[i])))
        return tmpret
    return False

def part2():
    output = 0
    for row in open('testinput.txt','r'):
        res = int(row.split(":")[0])
        values = [int(v) for v in row.strip().split(" ") if ":" not in v]
        if solve(res,values,0,0):
            output += res
    print(output)

part2()

#to low 5555508069823

#661823605105500