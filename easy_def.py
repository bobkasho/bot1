#easy me first def sample

def kick_scooter(name, weight):
    if weight < 60:
        print('Run, ',  name, ' Run!!!')
    else:
        print('O, No, Bro - You Are Very Heavy!')

name = input('Input Your Name: ')
weight = int(input('Input Your Weight in Kg: '))
kick_scooter(name, weight)

def drink_me(param):
    msq = ' В..ПИ:Ваем ' + param + ' сакан '
    print(msq)
    param = 'пусой '

qlass = 'попный '
drink_me(qlass)
print( ' Сакан ' , qlass )