#спроба зробити модуль заповнення даних про клієнта використовуючі набуті під час навчання знання

print('Картка клієнта')
# що мені цікаво - ввести ідентифікатор, ім'я, телефон(и), адресу тг, якісь додаткові данні - поки не знаю навіть які
# думаю треба використовати функцію. хоча може сам модуль і є по суті функцією. почнемо, а там побачимо

client_id = input('Please imput client id: ')
client_name = input('Please input Name: ')
client_phone = input('Please input phone number: ')
client_adress = input('Adress: ')
client_tg = input('Telegram: ')
# зібравши дані по клієнту, створюю список
client_inf = [client_id, client_name, client_phone, client_adress, client_tg]
# роздрукую за для перевірки
print(client_inf)
