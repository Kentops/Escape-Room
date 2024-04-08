from door import Door
import random

class Locked_Door(Door):
  '''The Locked Door'''
  def __init__(self):
    self.key_location = random.choice([
      "under the mat",
      "under the flower pot",
      "under the fake rock"
    ])
    self._key_found = False

  def examine_door(self):
    return "A locked door. The key is hidden nearby."
    
  def menu_options(self):
    return (
      "1. Look under the mat\n"
      "2. Look under the flower pot\n"
      "3. Look under the fake rock"
    )

  def get_menu_max(self):
    return 3

  def attempt(self, option):
    if option == 1 and self.key_location == "under the mat":
      self._key_found = True
      return "You found the key!"
    elif option == 2 and self.key_location == "under the flower pot":
      self._key_found = True
      return "You found the key!"
    elif option == 3 and self.key_location == "under the fake rock":
      self._key_found = True
      return "You found the key!"
    else:
      return "Yikes! No key here."

  def is_unlocked(self):
    return self._key_found

  def clue(self):
    return "Look somewhere else."

  def success(self):
    return "Congratulations! You've successfully unlocked the locked door."