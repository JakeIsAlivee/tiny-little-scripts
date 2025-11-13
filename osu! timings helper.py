print('This script is just a calculator for osu! sliders velocity multiplayer transitions.\nMade by JakeIsAlivee\n')

while True:
    try:
        print('Enter a number for the starting point\nDelete the floating point in your multiplyer. Example:\nYou have: 3,00. Enter: 300')
        startp = int(input())
        break
    except ValueError:
        print('\ndo you not know how to read?\n')
        continue
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
while True:
    print('Enter an operation to do for every step (subtraction/addition) (-/+)')
    whattodo = input()
    if whattodo.capitalize() == '-' or whattodo.capitalize() == '+':
        break
    if whattodo.capitalize()[0:8] == 'Subtract' or whattodo.capitalize()[0:3] == 'Add':
        print('\nPlease write only "-" or "+"\n')
        continue
    else:
        print('\ndo you not know how to read?\n')
        continue
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
while True:
    try:
        print('Enter a number that will be subtracted or added from the starting point and added to itself for every step. Formula (I guess?):\nx = 2, y = 1000, z = 2\nz = z + x\ny = y -/+ z')
        firstnum = int(input())
        break
    except ValueError:
        print('\ndo you not know how to read?\n')
        continue
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
print('Here is your numbers:')
secondnum = 0
if whattodo == '+':
    while startp <= 10000 and startp >= 0:
        secondnum = secondnum + firstnum
        print(str(startp)+' + '+str(secondnum)+' = '+str(startp+secondnum))
        startp = startp + secondnum
if whattodo == '-':
    while startp <= 10000 and startp >= 0:
        secondnum = secondnum + firstnum
        print(str(startp)+' - '+str(secondnum)+' = '+str(startp-secondnum))
        startp = startp - secondnum
print('You know what to do.')