def part1():
  lista = open('input.txt','r').readlines()
  output = 0
  for i in range(0,len(lista),4):
    a = [int(lista[i][12:14]),int(lista[i][18:20])]
    b = [int(lista[i+1][12:14]),int(lista[i+1][18:20])]
    p = [int(lista[i+2].split('=')[1].split(",")[0]),int(lista[i+2].split('=')[2])]

    for x in range(101):
      for y in range(101):
        if (a[0]*x+b[0]*y==p[0] and a[1]*x+b[1]*y==p[1]):
          output += x*3+y
          break

  print(output)

part1()