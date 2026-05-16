import random
import time
import datetime

snast = 5
jyk = 10
spining = 1
maxovka = 1
inv = []
my_market = False
money = 500
cost_1 = 50
cost_2 = 100
cost_3 = 150
class fish_spining:
    def __init__(self):
        self.name = random.choice(["Щука","Окунь", "Голавль", "Сеть"])
        self.weight = random.randint(500, 5000)
    
class fish_maxovoe:
    def __init__(self):
        self.name = random.choice(["Окунь", "Уклейка","Карп"])
        self.weight = random.randint(500, 4150)
        if self.name == "Уклейка":
            self.weight = random.randint(20, 110)

new_fish_maxovoe = fish_maxovoe()
new_fish_spiningovoe = fish_spining()
def fishing_spining():
    global snast, inv
    randomchek = random.randint(1, 3)
    if randomchek == 1:
        time.sleep(2)
        new_fish_spiningovoe = fish_spining()
        print(f"Ты поймал: {new_fish_spiningovoe.name}, вес: {new_fish_spiningovoe.weight}грамм")
        perevod1 = new_fish_spiningovoe.weight / 1000
        print(f"В кг это: {perevod1}")
        timer = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"А поймал ты эту рыбу в: {timer}")
        inv.append(new_fish_spiningovoe)
    elif randomchek == 2:
        time.sleep(2)
        print("Коряга. Ты потерял снасть.")
        snast -= 1
    if randomchek == 3:
        time.sleep(2)
        print("Ты поймал сеть, а в сети была одна колебалка! И сеть была слишком мелкой и ты ее просто выкинул на берег.")
        snast += 1


def fishing_maxavoe():
    global jyk, maxovka, inv
    randomchik = random.randint(1, 3)
    if randomchik == 1:
        time.sleep(2)
        new_fish_maxovoe = fish_maxovoe()
        print(f"Ты поймал: {new_fish_maxovoe.name}, вес: {new_fish_maxovoe.weight}")
        perevod2 = new_fish_maxovoe.weight / 1000
        print(f"В кг это: {perevod2}")
        timer2 = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Поймал рыбу по времени: {timer2}")
        inv.append(new_fish_maxovoe)
        if new_fish_maxovoe.weight >= 4000:
            print("Твоя удочка сломалась от такой рыбы. Она была очень тяжелой")
            maxovka -= 1
    elif randomchik == 2:
        time.sleep(2)
        print("Ты пытался подсечь рыбу, но она не клюнула!")
    elif randomchik == 3:
        time.sleep(2)
        print("Ты кинул, но не решил подсекать рыбу и она съела твоего опарыша.")
        jyk -= 1


def rinok():
    global money, snast, jyk, maxovka, spining, inv, my_market
    print("Добро пожаловать на рынок рыбы и покупки удилищ и снастей с жуками!")
    
    while my_market == True:
        print("Выбери чо сделаешь на рынке: 1 - продать рыбы. 2 - купить жуков. 3 - купить маховку. 4 - купить спининг. 5 - купить снасть. 6 - уйти с рынка. 7 - Посмотреть сколько монет")
        op2 = int(input())
        if op2 == 6:
            my_market = False
            break
            
        elif op2 == 1:
            print('Какую именно рыбу хочешь продать?')
            for fish in inv:
                print(f"- {fish.name} ({fish.weight}г)")
            print("Введи чо за рыбу вообще хочешь продать?")
            a = input()
            
            for fish in inv:
                if fish.name == a:
                    if fish.name == "Сеть":
                        print(f"Ты сдаешь мне сеть с весом {fish.weight}г")
                        idx = inv.index(fish)
                        inv.pop(idx)
                        money += 50
                        break
                    elif fish.weight <= 500:
                        print(f"Твоя рыба: {fish.name} с весом: {fish.weight}г продается")
                        idx = inv.index(fish)
                        inv.pop(idx)
                        money += cost_1
                        print("Продана!")
                        break
                    elif fish.weight <= 1500:
                        print(f"Твоя рыба: {fish.name} с весом: {fish.weight}г продается")
                        idx = inv.index(fish)
                        inv.pop(idx)
                        money += cost_2
                        print("Продана!")
                        break
                    elif fish.weight <= 5000:
                        print(f"Твоя рыба: {fish.name} с весом: {fish.weight}г продается")
                        idx = inv.index(fish)
                        inv.pop(idx)
                        money += cost_3
                        print("Продана!")
                        break

        elif op2 == 2:
            print("Сколько жуков купить хочешь?")
            buy_jyk = int(input())
            if money > 0:
                print('Да деньги у тебя есть чтобы купить жуков')
                if buy_jyk <= 5:
                    print("Щас насыпем тебе жуков")
                    money -= 25
                    jyk += 5
                    print("Готово")
                elif buy_jyk <= 10:
                    print("Щас насыпем тебе жуков")
                    money -= 50
                    jyk += 10
                    print("Готово")
                elif buy_jyk <= 15:
                    print("Щас насыпем тебе жуков")
                    money -= 75
                    jyk += 15
                    print("Готово")
                elif buy_jyk <= 20:
                    print("Щас насыпем тебе жуков")
                    money -= 100
                    jyk += 20 
                    print("Готово")
                elif buy_jyk >= 21:
                    print("Так слишком много за раз нельзя...")

        elif op2 == 3:
            print("Одна готовая маховка: 1000 рублей")
            if money >= 1000:
                print("Купить готовую маховку ты и вправду можешь!")
                money -= 1000
                maxovka += 1
                print("Успешно. Пользуйся на здоровье")
            else:
                print("Денег у тебя нету")

        elif op2 == 4:
            print("Ты пришел за спинингом. Готовый спининг стоит: 1500")
            if money >= 1500:
                print("Ты можешь его приобрести")
                money -= 1500
                spining += 1
                print("Успешно. Пользуйся на здоровье")
            else:
                print("Денег не хватает!")

        # 6. Покупка снастей
        elif op2 == 5:
            print("Ты пришел покупать снасти на спининг. Можно от 1 до 5:")
            buy_snast = int(input())
            if buy_snast > 5:
                print('Я же говорил не больше 5')
            elif buy_snast <= 0:
                print("Как ты можешь купить 0 снастей?")
            else:
                required_money = buy_snast * 100
                if money >= required_money:
                    money -= required_money
                    snast += buy_snast
                    print(f"Успешно куплено снастей: {buy_snast}")
                else:
                    print("Не хватает денег!")

        elif op2 == 7:
            print(f"Твой баланс: {money} монет.")

                     

print("Начинаем Рыбалку!")
while True:
    try:
        print("Выбери действие: 1 - Посмотреть инвентарь. 2 - закинуть спининг. 3 - закинуть маховое удилище. 4 - пойти на рынок и продать рыбу. 5 - посмотреть сколько денег. 6 - уйти с рыбалки. 7 - посмотреть сколько червей и снастей.")
        op = int(input())
        if op == 1 and inv != []:
            for fish in inv:
                print(f"- {fish.name} ({fish.weight}г)")
        elif op == 1 and inv == []:
            print("Там все пусто")
        elif op == 2:
            if spining >= 1:
                fishing_spining()
            elif spining <= 0:
                print('У тебя нету спининга!')
        elif op == 3:
            if maxovka >= 1:
                fishing_maxavoe()
            elif maxovka <= 0:
                print("У тебя нету махового удилища!")
            elif maxovka >= 1 and jyk <= 0:
                print("Удилище то есть, но нету насекомых а без них не будет рыба клювать твой крюк")
            elif maxovka <= 1 and jyk <= 0:
                print("Ни удилища, ни жука, иди покупай их чтобы ловить рыбки")
        elif op == 4:
            print("Идем на рынок!")
            time.sleep(2)
            my_market = True
            rinok()
        elif op == 5:
            print(money)
        elif op == 6:
            break
            input("Пока!")
        elif op == 7:
            print(f"У тебя червей: {jyk}, а снастей для спининга: {snast}")
    except ValueError:
        print("Вводи числа")
