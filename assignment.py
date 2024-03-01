print("For square pattern")
size = 5
for i in range(size):
    for j in range(size):
     print('*', end=' ')
    print()

print("For right angled triangle")
height = 5
for i in range(height):
   for j in range(i + 1):
      print('*', end='')
   print()  