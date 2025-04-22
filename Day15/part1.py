def movebox(map,y,x,my,mx):
  if map[y+my][x+mx] == ".":
    map[y+my][x+mx] = "O"
    return map, True
  elif map[y+my][x+mx] == "O":
    map, output = movebox(map,y+my,x+mx,my,mx)
    return map, output
  elif map[y+my][x+mx] == "#":
    return map, False

def part1():
  map = []
  moves = ""
  map_done = False
  for row in open('input.txt','r').readlines():
    if row == "\n":
      map_done = True
    elif map_done:
      moves += row
    else:
      map.append(list(row))

  robot = [0,0]
  for y in range(len(map)):
    for x in range(len(map[y])):
      if map[y][x] == "@":
        robot = [y,x]

  for m in moves:
    if m == "<" and robot[1]-1 >= 0:
      if map[robot[0]][robot[1]-1] == ".":
        map[robot[0]][robot[1]] = "."
        robot[1] -= 1
        map[robot[0]][robot[1]] = "@"
      elif map[robot[0]][robot[1]-1] == "O":
        map, changed = movebox(map,robot[0],robot[1],0,-1)
        if changed:
          map[robot[0]][robot[1]] = "."
          robot[1] -= 1
          map[robot[0]][robot[1]] = "@"
    elif m ==">" and robot[1]+1 < len(map[0]):
      if map[robot[0]][robot[1]+1] == ".":
        map[robot[0]][robot[1]] = "."
        robot[1] += 1
        map[robot[0]][robot[1]] = "@"
      elif map[robot[0]][robot[1]+1] == "O":
        map, changed = movebox(map,robot[0],robot[1],0,1)
        if changed:
          map[robot[0]][robot[1]] = "."
          robot[1] += 1
          map[robot[0]][robot[1]] = "@"
    elif m =="v" and robot[0]+1 < len(map):
      if map[robot[0]+1][robot[1]] == ".":
        map[robot[0]][robot[1]] = "."
        robot[0] += 1
        map[robot[0]][robot[1]] = "@"
      elif map[robot[0]+1][robot[1]] == "O":
        map, changed = movebox(map,robot[0],robot[1],1,0)
        if changed:
          map[robot[0]][robot[1]] = "."
          robot[0] += 1
          map[robot[0]][robot[1]] = "@"
    elif m =="^" and robot[0]-1 >= 0:
      if map[robot[0]-1][robot[1]] == ".":
        map[robot[0]][robot[1]] = "."
        robot[0] -= 1
        map[robot[0]][robot[1]] = "@"
      elif map[robot[0]-1][robot[1]] == "O":
        map, changed = movebox(map,robot[0],robot[1],-1,0)
        if changed:
          map[robot[0]][robot[1]] = "."
          robot[0] -= 1
          map[robot[0]][robot[1]] = "@"

  output = 0
  for y in range(len(map)):
    for x in range(len(map[y])):
      if map[y][x] == "O":
        output += 100*y+x

  print(output)

part1()