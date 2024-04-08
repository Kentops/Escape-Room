from door import Door
import random

class Combo_Door(Door):
  '''The Combo Door'''
  def __init__(self):
    self.combination = random.randint(1,10)
    self._unlocked = False
    
  def examine_door(self):
    return "A door with a combination lock. You can spin the dial to a number 1-10."

  def menu_options(self):
    return "Enter a # 1-10: "

  def get_menu_max(self):
    return 10
    
  def attempt(self, option):
    if option == self.combination:
      self._unlocked = True
      return "You entered the correct number!"
    elif option < self.combination:
      return "Too low."
    else:
      return "Too high."

  def is_unlocked(self):
    return self._unlocked

  def clue(self):
    return "Try a different number."

  def success(self):
    return "You found the correct value and opened the door."