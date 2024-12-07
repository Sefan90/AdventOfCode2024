def solve(res,values,i,calc):
    if calc == res and i == len(values):
        return True
    elif i < len(values):
        tmpret = solve(res,values,i+1,calc*values[i])
        if tmpret == False:
            tmpret = solve(res,values,i+1,calc+values[i])
        return tmpret
    return False

def part1():
    output = 0
    for row in open('input.txt','r'):
        res = int(row.split(":")[0])
        values = [int(v) for v in row.strip().split(" ") if ":" not in v]
        if solve(res,values,0,0):
            output += res
    print(output)

part1()