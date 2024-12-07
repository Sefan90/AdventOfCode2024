import re

def part1():
    output = 0
    file = open('input.txt','r')
    for row in file:
        for i in re.findall("mul\(\d{1,3},\d{1,3}\)",row):
            tmp = i.replace("mul(","").replace(")","").split(",")
            output += int(tmp[0])*int(tmp[1])

    print(output)

part1()