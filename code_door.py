from door import Door
import random

class Code_Door(Door):
  '''The Code Door'''

  def __init__(self):
    self._code = [random.choice([0, 1]) for _ in range (3)]
    self._input = [0,0,0]

  def examine_door(self):
    return (
      "A door with a coded keypad with three characters."
      "Each key toggles a value with an 'X' or an 'O'."
    )

  def menu_options(self):
    return (
      "1. Press Key 1\n"
      "2. Press Key 2\n"
      "3. Press Key 3"
    )

  def get_menu_max(self):
    return 3

  def attempt(self, option):
    if self._input[option - 1] == 0: #Flip value
      self._input[option - 1] = 1
    else:
      self._input[option - 1] = 0

    message = "The keypad now reads: "
    for i in range(0,3):
      if(self._input[i] == 0):
        message += "O"
      else:
        message += "X"
    return message

  def is_unlocked(self):
    return self._code == self._input

  def clue(self):
    numCorrect = 0
    for i in range(0,3):
      if(self._code[i] == self._input[i]):
        numCorrect += 1
    return f"{numCorrect} characters are correct."

  def success(self):
    return "Congratulations! You've successfully unlocked the code door."

