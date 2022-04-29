size = int(input())
height, width = size * 2, (size * 2) + 3
a, b, c, d, e, f, g = "(", ")", (chr(92)), "/", "|", ".", " "

number_increase, number_decrease, number_of_loop, num_dec_2 = 0, width-4, 0, size-4

for i in range(size):
  print(a + (f*number_increase) + c + str(g * ((number_decrease))) + d + (f*number_increase) + b)
  number_increase += 1
  number_decrease -= 2
  number_of_loop += 1
  if number_of_loop == height-(size+1):
      print(a + (f*number_increase) + c + str(g * ((number_decrease)-3)) + "G" + str(g * ((number_decrease)-3)) + d + (f*number_increase) + b)
      break
print(a + (f*number_increase) + d + str(g * ((number_decrease)-3)) + e + str(g * ((number_decrease)-3)) + c + (f*number_increase) + b)

for i in range(size-1):
  number_increase -= 1
  number_decrease += 1
  print(a + (f*number_increase) + d + (g*((number_decrease)-size+(size-1))) + e + (g*((number_decrease)-size+(size-1))) + c + (f*number_increase) + b)