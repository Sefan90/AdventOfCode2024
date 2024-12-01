def part1():
    file = open('input.txt','r')
    output = 0
    list1 = []
    list2 = []
    for row in file:
        tmprow = row.split("   ")
        list1.append(int(tmprow[0]))
        list2.append(int(tmprow[1]))
    list1.sort()
    list2.sort()
    for i in range(len(list1)):
        output += abs(list1[i]-list2[i])
    print(output)

part1()