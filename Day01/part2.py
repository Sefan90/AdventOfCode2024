def part2():
    file = open('input.txt','r')
    output = 0
    list1 = []
    list2 = []
    for row in file:
        tmprow = row.split("   ")
        list1.append(int(tmprow[0]))
        list2.append(int(tmprow[1]))
    for i in list1:
        output += (i*list2.count(i))
    print(output)

part2()