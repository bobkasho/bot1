#test for auto system v. 0.01 BobKash
import random

models = ['AC', 'Acura', 'Alfa Romeo', 'Alpina', 'Alpine', 'Aro', 'Asia', 'Aston Martin', 'Audi', 'Austin', 'BAW', 'Beijing', 'Bentley', 'BMW', 'Brilliance', 'Bristol', 'Bugatti', 'Buick', 'BYD', 'Богдан', 'Vector', 'Venturi', 'Volkswagen', 'Volvo', 'Vortex', 'Wartburg', 'Westfield', 'Wiesmann', 'Wuling', 'ВАЗ', '(Lada)', 'Geely', 'Geo', 'GMC', 'Great', 'Wall', 'ГАЗ', 'Dacia', 'Dadi', 'Daewoo', 'Daihatsu', 'Daimler', 'Dallas', 'Derways', 'De', 'Tomaso', 'Dodge', 'Dong Feng', 'Doninvest', 'Jeep', 'Jiangling', 'Jiangnan', 'Eagle', 'Zastava', 'ZX', 'ЗАЗ', 'ЗИЛ', 'Infiniti', 'Innocenti', 'Invicta', 'Iran Khodro', 'Isdera', 'Isuzu', 'IVECO', 'Xin', 'Kai', 'ИЖ', 'Cadillac', 'Callaway', 'Carbodies', 'Caterham', 'Citroen', 'Cizeta', 'Coggiola', 'Kia', 'Koenigsegg', 'Qvale', 'КАМАЗ', 'Lamborghini', 'Lancia', 'Land', 'Rover', 'Landwind', 'Lexus', 'Lifan', 'Lincoln', 'Lotus', 'LTI', 'Luxgen', 'ЛуАЗ', 'Mahindra', 'Marcos', 'Marlin', 'Marussia', 'Maruti', 'Maserati', 'Maybach', 'Mazda', 'McLaren', 'Mega', 'Mercedes-Benz', 'Mercury', 'Metrocab', 'MG', 'Minelli', 'Mini', 'Mitsubishi', 'Mitsuoka', 'Monte', 'Carlo', 'Morgan', 'Москвич', 'Nissan', 'Noble', 'Oldsmobile', 'Opel', 'Pagani', 'Panoz', 'Paykan', 'Perodua', 'Peugeot', 'Plymouth', 'Pontiac', 'Porsche', 'Premier', 'Proton', 'Puma', 'Reliant', 'Renault', 'Rolls-Royce', 'Ronart', 'Rover', 'Saab', 'Saleen', 'Samsung', 'Saturn', 'Scion', 'SEAT', 'Skoda', 'SMA', 'Smart', 'Soueast', 'Spectre', 'SsangYong', 'Subaru', 'Suzuki', 'СеАЗ', 'Talbot', 'Tata', 'Tatra', 'Tianma', 'Tofas', 'Toyota', 'Trabant', 'TVR', 'УАЗ', 'FAW', 'Ferrari', 'Fiat', 'Ford', 'FSO', 'Fuqi', 'Hafei', 'Haima', 'Hindustan', 'Holden', 'Honda', 'HuangHai', 'Hummer', 'Hyundai', 'Chana', 'ChangFeng', 'Changhe', 'Chery', 'Chevrolet', 'Chrysler', 'Shifeng', 'ShuangHuan', 'JAC']

you_model = input('Enter Your Car Model Please: ')

print(models.index(you_model))

answer = input('Бажаєш дізнатись яку марку авто підібрав для тебе бот? Hапиши "yes" або "no": ')
bot_select = random.choice(models)
if answer == 'yes':
    print('Бот вважає, що тобі пасує: ' + bot_select)
else:
    print('А якби обрав - тобі б її подарували, дурнику')


#print(models[2])