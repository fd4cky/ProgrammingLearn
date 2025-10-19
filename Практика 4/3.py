tovars = { # товар: [цена, кол-во, категория]
    'apple': [24, 50, 'fruits'],
    'bananos': [30, 10, 'fruits'],
    'baklagan': [12, 33, 'vegetables'],
    'potatos': [8, 121, 'vegetables']
}
users = {
    'user': {
        'total': 0, # Суммарный чек юзера
        'apple': 3, # История покупок
        'bananos': 4
    }
}


class Product():
    def __init__(self, title):
        self.title = title

    @property
    def category(self):
        return tovars[self.title][2]

    @property
    def price(self):
        return tovars[self.title][0]

    @property
    def is_avaible(self):
        return True if tovars[self.title][1] > 0 else False


class Order(Product):
    def __init__(self, title, count, username):
        super().__init__(title)
        self.count = count
        self.username = username

    def buy(self):
        if self.username in users.keys():
            if super().is_avaible: # проверяем на наличие товара
                price = round((super().price * self.count) * 1.2, 1) # считаем цену с учетом НДС в 20%
                users[self.username] = users.get(self.username, {'total': 0}) # если юзер впервые покупает, добавляем в базу
                tovars[self.title][1] -= self.count # из кол-ва товара вычитаем те, что купили
                users[self.username][self.title] = users[self.username].get(self.title, 0) + self.count # добавляем в историю товаров купленный товар
                users[self.username]['total'] += price # добавляем в тотал чек юзера, чек с покупки
                return price 
            else:
                return f'Товар не в наличии'
        else:
            return f'Пользователь не найден'
            

class Customer():
    def __init__(self, username):
        self.username = username

    @property
    def userinfo(self):
        if self.username in users.keys():
            user = users[self.username] #возвращаем сумму, которую юзер потратил и историю товаров
            return f'{self.username} потратил суммарно {user['total']}, купив \n{"\n".join([f"{y} {x}" for x, y in list(user.items())[1:]])}'
        return f'Пользователь не найден'
    
    def __str__(self):
        return self.userinfo


class ShoppingCart(Product):
    def __init__(self, title):
        super().__init__(title)

    def add(self, count): # добавлять кол-во товара
        tovars[self.title][1] += count
        return tovars[self.title][1]
    
    def minus(self, count): # удаляем кол-во товара
        tovars[self.title][1] = max(tovars[self.title][1] - count, 0) # проверяем чтобы не было отриц. кол-ва
        return tovars[self.title][1]
    
    def update(self, count): # обновляем кол-во товара
        tovars[self.title][1] = count
        return tovars[self.title][1]
    
    def __str__(self):
        return str(tovars[self.title][1])


tovar = Product('apple')
order = Order('apple', 4, 'user')
user = Customer('user')
cart = ShoppingCart('apple')

print(f'Изначальное количество яблок {cart}, по цене за штуку {tovar.price}')
print(f'купили 4 яблока за {order.buy()}')
print(user)
print(f'Количество яблок после покупки {cart}')
cart.add(1000)
print(f'Добавили 1000 яблок и стало {cart} яблок')