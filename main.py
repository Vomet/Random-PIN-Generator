from random import randint
# allows user to repeat program
import printBox

def repeat_program():
  repeat = input("Repeat program? [Y/n]: ")
  if repeat == 'y' or repeat == 'Y' or repeat == '':
    start()
    repeat = ""
  elif repeat == 'n' or repeat == 'N':
    print("Program terminated.")
  else:
    print("Enter a valid keystroke.")
    repeat_program()

def pin_gen(length):
  ask_user = str(input("Generate a PIN? [Y/n]: "))
  if ask_user == 'y' or ask_user == "Y" or ask_user == '':
    random_pin = ''
    for i in range(length): # generator part
      random_num = str(randint(0, 9))
      random_pin += random_num
    print(printBox.printBox(random_pin))
    pin_gen(length)
  elif ask_user == 'n' or ask_user == 'N':
    repeat_program()
  else:
    print("Enter a valid keystroke.")
    pin_gen(length)

def pin_length():
  try:
    length = int(input("Enter length of PIN: "))
  except:
    print("Enter a number.")
    hold = pin_length() # allows input of this to be saved
    """ \
      visualization here: 
      http://www.pythontutor.com/visualize.html#code=from%20random%20import%20randint%0Adef%20pin_gen%28length%29%3A%0A%20%20ask_user%20%3D%20str%28input%28%22Generate%20a%20PIN%3F%20%5BY/n%5D%3A%20%22%29%29%0A%20%20if%20ask_user%20%3D%3D%20'y'%20or%20ask_user%20%3D%3D%20%22Y%22%20or%20ask_user%20%3D%3D%20''%3A%0A%20%20%20%20random_pin%20%3D%20''%0A%20%20%20%20for%20i%20in%20range%28length%29%3A%0A%20%20%20%20%20%20random_num%20%3D%20str%28randint%280,%209%29%29%0A%20%20%20%20%20%20random_pin%20%2B%3D%20random_num%0A%20%20%20%20print%28random_pin%29%0A%20%20%20%20pin_gen%28%29%0A%20%20elif%20ask_user%20%3D%3D%20'n'%20or%20ask_user%20%3D%3D%20'N'%3A%0A%20%20%20%20print%28%22Program%20terminated.%22%29%0A%0Adef%20pin_length%28%29%3A%0A%20%20try%3A%0A%20%20%20%20length%20%3D%20int%28input%28%22Enter%20length%20of%20PIN%3A%20%22%29%29%0A%20%20except%3A%0A%20%20%20%20print%28%22Enter%20a%20number.%22%29%0A%20%20%20%20hold%20%3D%20pin_length%28%29%20%23%20allows%20input%20of%20this%20to%20be%20saved%0A%20%20%20%20return%20hold%0A%20%20else%3A%0A%20%20%20%20return%20length%0A%0Alength%20%3D%20pin_length%28%29%0A%0Apin_gen%28length%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
      """
    return hold
  else:
    return length

def start(): # starts all functions in one
  length = pin_length()
  pin_gen(length)
start()
