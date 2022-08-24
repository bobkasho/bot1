#easy me first def sample

def kick_scooter(name, weight):
    if weight < 60:
        print('Run, ',  name, ' Run!!!')
    else:
        print('O, No, Bro - You Are Very Heavy!')

name = input('Input Your Name: ')
weight = int(input('Input Your Weight in Kg: '))
kick_scooter(name, weight)
