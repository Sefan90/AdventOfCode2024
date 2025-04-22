def part2():
  lista = open('input.txt','r').readlines()
  output = 0
  for i in range(0,len(lista),4):
    a = [int(lista[i][12:14]),int(lista[i][18:20])]
    b = [int(lista[i+1][12:14]),int(lista[i+1][18:20])]
    p = [int(lista[i+2].split('=')[1].split(",")[0])+10000000000000,int(lista[i+2].split('=')[2])+10000000000000]
    tmpa = [a[0]*b[1],a[1]*b[0]]
    tmpp = [p[0]*b[1],p[1]*b[0]]
    pressa = (tmpp[0]-tmpp[1])/(tmpa[0]-tmpa[1])
    pressb = (p[0]-a[0]*(pressa))/b[0]
    if pressa == int(pressa) and pressb == int(pressb):
      output += pressa*3+pressb
  print(int(output))

part2()