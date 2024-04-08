import random
from door import Door

class Deadbolt_Door(Door):
  '''
  The Deadbolt Door
  int _bolt1: The state of the first bolt.
  int _bolt2: The state of the second bolt.
  '''
  def __init__(self):
    super().__init__()
    self._bolt1 = random.randint(0,1)
    self._bolt2 = random.randint(0,1)
  
  def examine_door(self):
    return "a door with two deadbolts. Both bolts need to be unlocked for the door to open, but you cannot tell if either bolt is locked or unlocked."

  def menu_options(self):
    return "1. Toggle Bolt 1\n2. Toggle Bolt 2"

  def get_menu_max(self):
    return 2

  def attempt(self, option):
    if option == 1:
      self._bolt1 = 1 - self._bolt1
    elif option == 2:
      self._bolt2 = 1 - self._bolt2
    return "You toggle bolt {}.".format(option)

  def is_unlocked(self):
    return self._bolt1 == 0 and self._bolt2 == 0

  def clue(self):
    if self._bolt1 == 1 and self._bolt2 == 1:
      return "Both bolts appear locked."
    else:
      return "It seems like one bolt is locked"

  def success(self):
    return "You unlocked both deadbolts and opened the door."