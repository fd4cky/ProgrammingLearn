import requests


class Manager:
    """Класс для управления командой покемонов через PokeAPI."""

    team = dict()

    def __init__(self, pokemons: list = None):
        """Создает объект менеджера команды покемонов.

        Args:
            pokemons (list, optional): Список имен покемонов для добавления
                при инициализации. По умолчанию None.
        """
        if pokemons is None:
            pokemons = []
        for pokemon in pokemons:
            self.add(pokemon)

    def add(self, pokemon: str):
        """Добавляет покемона в команду, если его там еще нет.

        Args:
            pokemon (str): Имя покемона.
        """
        resp = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}').json()
        name = resp['name']
        if name in self.team:
            return
        self.team[name] = {
            'id': resp['id'],
            'base_experience': resp['base_experience'],
            'height': resp['height'],
            'weight': resp['weight'],
            'base_stat': resp['stats'][0]['base_stat'],
            'effort': resp['stats'][0]['effort'],
        }

    def delete(self, pokemon: str):
        """Удаляет покемона из команды по имени.

        Args:
            pokemon (str): Имя покемона для удаления.
        """
        self.team.pop(pokemon, None)

    def info(self, pokemon: str = ''):
        """Возвращает красиво отформатированную информацию о покемонах команды.

        Args:
            pokemon (str, optional): Имя покемона. Если не указано,
                возвращается информация обо всей команде.

        Returns:
            str: Отформатированная строка с данными.
        """
        if not self.team:
            return 'Команда пуста.'

        def format_poke(name, data):
            return (
                f"\nИмя: {name.capitalize()}\n"
                f"  ID: {data['id']}\n"
                f"  Опыт: {data['base_experience']}\n"
                f"  Рост: {data['height']}\n"
                f"  Вес: {data['weight']}\n"
                f"  Базовая сила: {data['base_stat']}\n"
                f"  Усилие: {data['effort']}\n"
            )

        if pokemon == '':
            result = 'Команда покемонов:\n'
            for name, data in self.team.items():
                result += format_poke(name, data)
            return result.strip()

        pokemon = pokemon.lower()
        data = self.team.get(pokemon)
        if not data:
            return f"Покемон {pokemon} не найден в команде."

        return format_poke(pokemon, data).strip()

    def find(self, pokemon: str):
        """Находит покемона по имени в команде.

        Args:
            pokemon (str): Имя покемона.

        Returns:
            dict | None: Данные о покемоне, если найден.
        """
        return self.team.get(pokemon)

    def battle(self, pokemon1: str, pokemon2: str):
        """Проводит тренировочный бой между двумя покемонами.

        Args:
            pokemon1 (str): Имя первого покемона.
            pokemon2 (str): Имя второго покемона.

        Returns:
            str | None: Имя победителя, 'ничья' или None,
                если один из покемонов отсутствует.
        """
        if pokemon1 not in self.team or pokemon2 not in self.team:
            return None

        p1 = self.team[pokemon1]
        p2 = self.team[pokemon2]

        score1 = p1['base_experience'] + p1['base_stat'] + p1['effort']
        score2 = p2['base_experience'] + p2['base_stat'] + p2['effort']

        if score1 > score2:
            return pokemon1
        elif score1 < score2:
            return pokemon2
        return 'ничья'
    
    def __str__(self):
        return self.info()


test = Manager(['ditto'])

# Добавляем еще покемонов в команду
test.add('pikachu')
test.add('bulbasaur')

# Просмотр информации о всей команде
print('Команда:')
print(test.info())

# Пример боя между покемонами, которые есть в команде
print('\nБой:')
winner = test.battle('pikachu', 'ditto')
if winner is None:
    print('Один из покемонов отсутствует в команде.')
elif winner == 'ничья':
    print('Ничья!')
else:
    print(f'Победил: {winner}')