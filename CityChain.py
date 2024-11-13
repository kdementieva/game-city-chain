import random

f = open('cities.txt', encoding='utf8')
cities_list = [line.strip() for line in f]
f.close()

answers = []

def get_city(letter = ''):
    if letter != '':
        cities = [city for city in cities_list if city.startswith(letter.upper())]
        while True:
            line_rnd = random.randint(0, len(cities) - 1)
            city = cities[line_rnd]
            if city not in answers:
                break
            else:
                cities.remove(city)
                if not cities:
                    return False

    else:
        line_rnd = random.randint(0, len(cities_list) - 1)
        city = cities_list[line_rnd]
    answers.append(city)
    return city

def check_city(user_city, opponent_city):
    if user_city not in cities_list:
        print('Такого города не существует')
        return False
    if user_city in answers:
        print('Такой город уже использовался')
        return False
    letter = opponent_city[-1]
    if letter in ['ь', 'ъ', 'ы']:
        letter = opponent_city[-2]
    if user_city[0].lower() != letter.lower():
        print('Нужно назвать город на последнюю букву')
        return False
    answers.append(user_city)
    return True
              
current_city = get_city()
print('Игра в города. Мой ход: ')
print(current_city)
mistakes = 0
while True:
    user_city = input('Твоя очередь: ').title()
    if check_city(user_city, current_city):
        letter = user_city[-1]
        if letter in ['ь', 'ъ', 'ы']:
            letter = user_city[-2]
        current_city = get_city(letter)
        if not current_city:
            print('Не могу найти подходящий город. Ты победил!')
            break
        print(current_city)
    else:
        if mistakes == 5:
            print('5 неудачных попыток. игра окончена, ты проиграл!')
            break
        else:
            mistakes += 1
            print(f'Попробуй еще раз, у тебя {6 - mistakes} попыток')
        
f = open('answers.txt', 'w', encoding='utf8')
for ans in answers:
    f.write(ans + '\n')
f.close()