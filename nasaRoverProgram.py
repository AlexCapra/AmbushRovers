import rover

def movingRovers(fileName):
  f = open(fileName,'r')

  plateau = f.readline().split()
  while True:
    roverLine = f.readline().split()
    moveCommands = f.readline()
    if not moveCommands: break #EOF

    #print('RoverLine: ', roverLine)
    #print('moveCommands: ', moveCommands)

    r = rover.rover(int(roverLine[0]),int(roverLine[1]),roverLine[2], int(plateau[0]), int(plateau[1]))
    #print(r)
    for command in moveCommands:
      r.move(command)
    print(r)


   


