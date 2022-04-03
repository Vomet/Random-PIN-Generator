def printBox(input):
  input = "│  " + str(input) + "  │"
  width = len(input)-2
  # top part of box
  print("┌", end='')
  i = 0
  while i < width:
    print("─", end='')
    i += 1
  print("┐", end='')

  print("\n" + input)
  # bottom part of box
  print("└", end='')
  i = 0
  while i < width:
    print("─", end='')
    i += 1
  print("┘")

  return ''
