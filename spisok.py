spisok = ['ого-го', 'ну таке...', 'ти так вважаєш?', 'маєш рацію', 'мабуть в цьому є сенс', 'можливо і так', 'я хз', 'що тобі відповісти?', 'ти щось не те кажеш', 'так!!!', 'о ноу!', 'ти знову за старе?!', 'мені треба подумати', 'ти ще тут? міцний горішок )))', 'з тобою кумедно', 'ой дурне...', 'іди похрумкай барбарисок']

summ_spisok = len(spisok)
print('List phrases:')

big_text = 'a'

i = -1
#while i < summ_spisok:
    #i = i + 1
    #print('Its phraze number' + str(i), spisok[i])
for i in range(summ_spisok):
    print('Its phraze number' + str(i), spisok[i])
    if spisok[i] > big_text:
        big_text = spisok[i]

print('Summary phrases: ', summ_spisok)
print('Bigest phrase: ' + big_text)
print('Отака ку*ня, малята :-)')