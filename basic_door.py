from door import Door
import random

class Basic_Door(Door):
  '''
  The Basic Door\n
  int _state: 0 for push, 1 for pull
  int _input: The user's input
  '''

  def __init__(self):
    '''Constructs a basic door'''
    self._state = random.randint(1,2)

  def examine_door(self):
    return "a basic door. You can either push it or pull it to open."

  def menu_options(self):
    return "1. Push\n2. Pull"

  def get_menu_max(self):
    return 2

  def attempt(self, option):
    self._input = option #Defines _input
    temp = "push" if option == 1 else "pull"
    return f"You {temp} on the door."

  def is_unlocked(self):
    return self._state == self._input

  def clue(self):
    return "Try the other way."

  def success(self):
    return "You opened the door."

