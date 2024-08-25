print('''
   ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/


 ''')



print('welcome to Treasure Island\n')
print('your mission is to find the treasure\n')

print('there are two roads ahead!!!, move left or right\n')

road = input('which road do you choose left or right?\n: ')

road = road.lower()

if road == 'left':
  print('you walked for a while on the left road...\n')
  print('the end of the road is a river...\n')
  print('do you want swim or wait...\n')

  river = input('which do you choose swim or wait?\n: ')

  river = river.lower()

  if river == 'wait':
    print('\nyou waited till night...\n')
    print('you seemed lost and confused...\n')
    print("Suddenly!!!, you noticed a boat from afar...\n")
    print('the boat helped you to cross the river...\n')

    print('There is a island in the middle of the river...\n')
    print('which has three doors!!!\n')
    print('one red, one yellow and one blue\n')
    door = input('which door do you choose red, yellow or blue?\n: ')

    door = door.lower()

    if door == 'red':
      print("you enter a room with lot of gold and jewels!!!\n")
      print("YOU WIN!!!\n")
      print('Winner o o o, A pe la ye, Winner o o o ....\n')

    elif door == 'yellow':
      print("you entered a room but its empty\n")
      print("but there a a map to find your way home\n")

    elif door == 'blue':
      print("you entered a room but its empty\n")
      print("but there is no map, just a rope, boat and a ladder\n")

    else:
      print('you shot yourself!!!\n')
      print('Next time, follow instructions and try again\n')


  elif river == 'swim':
    print('you swam in the river for a while...\n')
    print('then you noticed  bubbles on the river...\n')
    print('behold you are eaten by a river monster!!!!\n')

    print('game over, you lost\n')

  else:
    print('invalid input, you VANISHED!!!\n')


else:
  print('you fell into a hole,  Sorry Try again\n')