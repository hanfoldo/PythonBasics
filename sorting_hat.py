griffondor = 0
slitherin = 0
ravenclaw = 0
hufflepuff = 0

print('q1 do you like: ')
 
print('1. dawn')
print('2. dusk')
answer = int(input('Enter answer (1-2): '))

if answer == 1:
    griffondor += 1
    ravenclaw += 1
elif answer == 2:
    slitherin += 1
    hufflepuff += 1
else:
    print('wrong asnwer boi')

#-------------------------------------------------q2-------------------------------------------------------------------------------

print('what do you want to be remembered as when you die:')

print('1. the great')
print('2. the good')
print('3. the bold')
print('4. THE WISE')

answer = int(input('Enter answer (1-4): '))

if answer == 1:
    slitherin += 1
elif answer == 2:
     hufflepuff+= 1
elif answer == 3:
    griffondor += 1

elif answer == 4:
    ravenclaw
else:
    print('wrong aswer boi')

    

print(' Which kind of instrument most pleases your ear?')
print('1. violin')
print('2. trumpet')
print('3. piano')
print('4. drums')

answer = int(input('Enter answer (1-4): '))

if answer == 1:
    slitherin += 1
elif answer == 2:
    hufflepuff += 1
elif answer == 3:
    ravenclaw += 1
elif answer == 4:
    griffondor += 1
else:
    print(' wrong answer boi')

print("Gryffindor: ", griffondor)
print("Ravenclaw: ", ravenclaw)
print("Hufflepuff: ", hufflepuff)
print("Slytherin: ", slitherin)

if griffondor >= ravenclaw and griffondor >= hufflepuff and griffondor >= slitherin:
  print('🦁 Gryffindor!')
elif ravenclaw >= hufflepuff and ravenclaw >= slitherin:
  print('🦅 Ravenclaw!')
elif hufflepuff >= slitherin:
  print('🦡 Hufflepuff!')
else:
  print('🐍 Slytherin!')

