import re

def part2():
    output = 0
    enabled = True
    file = open('input.txt','r')
    for row in file:
        for i in re.findall("mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)",row):
            if i == "do()":
                enabled = True
            elif i == "don't()":
                enabled = False
            elif enabled == True:
                tmp = i.replace("mul(","").replace(")","").split(",")
                output += int(tmp[0])*int(tmp[1])

    print(output)

part2()