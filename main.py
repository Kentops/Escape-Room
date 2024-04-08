from basic_door import Basic_Door
from code_door import Code_Door
from combo_door import Combo_Door
from deadbolt_door import Deadbolt_Door
from locked_door import Locked_Door
import random
import check_input

'''
Escape Room
3/19/2024
A program that simulates an escape room.
The user must open three doors randomly chosen from several different types.
'''

def open_door(door):
  '''Passes a door the user will try to open'''
  print("You encounter " + door.examine_door())
  unlocked = False
  while not unlocked:
    print(door.menu_options())
    player_input = check_input.get_int_range("", 1, door.get_menu_max())
    print(door.attempt(player_input))
    unlocked = door.is_unlocked()
    if unlocked:
      print(door.success())
    else:
      print(door.clue())
    print()

def main():
  doors = [
    Basic_Door(),
    Code_Door(), 
    Combo_Door(), 
    Deadbolt_Door(), 
    Locked_Door()
  ]
  
  random.shuffle(doors)
  print("Welcome to the escape room.\nYou must unlock 3 doors to escape...")
  for i in range(3): #This prevents referencing the same object
    the_door = doors[i]
    open_door(the_door)
  print("Congratulations! You have escaped... this time.")

main()