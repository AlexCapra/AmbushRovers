class direction( object ):
  def __init__(self, value):
    self.valueList = ['N', 'E', 'S', 'W']
    try:
      self.valueIdx = self.valueList.index(value)
      self.direction = value
    except IndexError:
      print('Invalid direction:', str(value))

  # Turns direction one position to the left or to the right. Ex: N to E for Right, and E to S for Left
  def turn(self, direction):
    if(direction == 'R'):
      if(self.valueIdx < len(self.valueList)):
        self.valueIdx += 1
      else:
        self.valueIdx = 0
    elif(direction == 'L'):
      if(self.valueIdx > 0):
        self.valueIdx -= 1
      else:
        self.valueIdx = len(self.valueList)-1
    self.direction = self.valueList[self.valueIdx]

  def __str__(self):
    return self.direction



class rover( object ):
  def __init__(self, initialPosX, initialPosY, initialFacingPos, plateauX, plateauY): 
    self.X = initialPosX
    self.Y = initialPosY
    self.facingPos = direction(initialFacingPos)
    self.limitX = plateauX
    self.limitY = plateauY

  # Parses move controls. 'L' and 'R' turn the rover left and right. 'M' moves the rover one space in the current facing position
  def move(self,moveControl):
    if(moveControl == 'R' or moveControl == 'L'):
      self.facingPos.turn(moveControl)
    elif(moveControl == 'M'):
      if(self.facingPos.direction == 'N'):
        if(self.Y + 1 <= self.limitX):
          self.Y += 1
      elif(self.facingPos.direction == 'E'):
        if(self.X + 1 <= self.limitY):
          self.X += 1
      elif(self.facingPos.direction == 'S'):
        if(self.Y - 1 >= 0):
          self.Y -= 1
      elif(self.facingPos.direction == 'W'):
        if(self.X - 1 >= 0):
          self.X -= 1


  def __str__( self ):
    return str(self.X) + ' ' + str(self.Y) + ' ' + str(self.facingPos)

