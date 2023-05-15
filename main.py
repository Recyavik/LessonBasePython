# Клас Блюдо (номер, название, вес, цена, время приготовления, белки, жиры, углеводы, ккалории)
class Dish:
    def __init__(self, number, name, weight, price, time, squir, fats, carbo, kcalories):
        self.number = number
        self.name = name
        self.weight = weight
        self.price = price
        self.time = time
        self.squir = squir
        self.fats = fats
        self.carbo = carbo
        self.kcalories = kcalories

    #   def __del__(self):
    #        print(self.name, '- удален')

    def ShowDish(self):
        if self.number is not None:
            print(str(self.number) + '.', self.name, '- Вес:' + str(self.weight), 'Ккал:' + str(self.kcalories), 'Цена:'
                  + str(self.price))


# Функция Считывание меню из файла, создание массива блюд в виде экземпляров объекта
def GetMenuFile(namefile):
    menulist = []
    with open(namefile, 'r', encoding='UTF-8') as fMenu:
        for line in fMenu:
            st = line.strip()
            st = st.split(',')
            obj = Dish(number=st[0], name=st[1], weight=st[2], price=st[3], time=st[4],
                       squir=st[5], fats=st[6], carbo=st[7], kcalories=st[8])
            menulist.append(obj)
    fMenu.close()
    return menulist


def WriteOrdersFile(namefile, arr):
    with open(namefile, 'a+', encoding='UTF-8') as fOrder:
        indx = 0
        for row in range(0, len(arr)):
            summa = 0
            fOrder.write('Столик №' + str(arr[row][0]) + ', ')
            m = len(arr[row])
            for j in range(1, m):
                indx = int(arr[row][j])
                if menuListCafe[indx - 1].number is not None:
                    summa += float(menuListCafe[indx - 1].price)
            fOrder.write(str(summa) + '\n')
    fOrder.close()


# Функция добавления блюда к заказу
def OrderFood(numbertable):
    order = [numbertable]
    print('Назовите номера блюд, которые хотите заказать (0 - завершить заказ):')
    number = int(input('Что выбрали: '))
    while number != 0:
        order.append(number)
        number = int(input('Что еще выбрали: '))
    return order


# Показать любой двухмерный массив (для тестирования)
def ShowAllMass(arr):
    for row in range(0, len(arr)):
        for j in range(1, len(arr[row])):
            print(arr[row][j], end=' ')
        print()


# Показать все заказы кафе
def ShowAllOrders(arr):
    for row in range(0, len(arr)):
        print('Столик №' + str(arr[row][0]))
        m = len(arr[row])
        for j in range(1, m):
            indx = arr[row][j]
            if menuListCafe[indx - 1].number is not None:
                menuListCafe[indx - 1].ShowDish()


# Показать итоги: Все заказы, Сумму, Калории, Время приготовления
def ShowItogs(arr, is_sum, is_calories, is_time):
    indx = 0
    for row in range(0, len(arr)):
        summa = 0
        calories = 0
        time: int = 0
        print('Столик №' + str(arr[row][0]))
        m = len(arr[row])
        for j in range(1, m):
            indx = int(arr[row][j])
            if menuListCafe[indx - 1].number is not None:
                summa += float(menuListCafe[indx - 1].price)
                calories += float(menuListCafe[indx - 1].kcalories)
        if is_sum:
            print('К оплате за этот заказ = ', summa, 'руб.')
        if is_calories:
            print(f'Калорийность этого заказа = {calories:4.2f}', 'кКал.')
        if is_time:
            if int(menuListCafe[indx - 1].time) >= time:
                time = int(menuListCafe[indx - 1].time)
            print('Время выполнения заказа =', time, 'мин.')
        return summa


# Запрос меню из файла, получение массива блюд в виде экземпляров объекта
menuListCafe = GetMenuFile('Menu.txt')
print('Наше меню: '.center(50))
for i in range(0, len(menuListCafe)):
    menuListCafe[i].ShowDish()

orders_all = []
# Сбор заказoв
number_table = int(input('Введите номер столика в кафе: (0 - завершить заказы) '))
while number_table != 0:
    orderTable = OrderFood(number_table)
    orders_all.append(orderTable)
    print('Записал. Ваш заказ:')
    print('Столик №', number_table)
    print(orderTable)
    for i in range(1, len(orderTable)):
        index = orderTable[i]
        menuListCafe[index - 1].ShowDish()
    number_table = int(input('Введите номер следующего столика или (0 - завершить заказы) '))

ShowAllOrders(orders_all)
s = ShowItogs(orders_all, True, False, False)
s2 = ShowItogs(orders_all, False, True, True)
WriteOrdersFile('Payments.txt', orders_all)
