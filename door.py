import abc

class Door(abc.ABC):
  '''
  The Door interface\n
  examine_door() -> str: Door description
  menu_options() -> str: The options
  get_menu_max() -> int: The number of options
  attempt(option) -> str: The user's selected option
  is_unlocked() -> bool: checks to see if the door was unlocked
  clue() -> str: A hint after a unsuccessful attempt.
  success(): congratulatory message
  '''

  @abc.abstractmethod
  def examine_door(self) -> str:
    '''Door description'''
    pass

  @abc.abstractmethod
  def menu_options(self) -> str:
    '''The options a player can chose from'''
    pass

  @abc.abstractmethod
  def get_menu_max(self) -> int:
    '''The number of menu options'''

  @abc.abstractmethod
  def attempt(self, option:int) -> str:
    '''Uses the user's menu option to update the attributes that determine whether the door is locked or unlocked. Returns a string of what was attempted'''
    pass

  @abc.abstractmethod
  def is_unlocked(self) ->bool:
    '''Checks attributes to see if the door should be unlocked'''

  @abc.abstractmethod
  def clue(self) -> str:
    '''A clue after an unsuccessful attempt'''
    pass

  @abc.abstractmethod
  def success(self) -> str:
    '''A congratulatory message for after the user opens the door'''

  