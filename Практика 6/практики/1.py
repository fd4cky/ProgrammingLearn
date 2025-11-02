import requests


# Из запроса получаем name и id покемона, создаем словарь вида {name: id}
pokemons = dict()
response = requests.get('https://pokeapi.co/api/v2/ability/?limit=20&offset=20')

for pokemon in response.json()['results']:
    pokemons[pokemon['name']] = pokemon['url'].split('/')[-2]

print(' '.join([name for name in pokemons.keys()]))

name = input('\nИмя покемона: ')

# Создаем запрос и вместо name указываем id покемона
pokemon_info = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemons[name]}/').json()

# Получаем нужные данные
result = {
    'Тип': pokemon_info['types'][0]['type']['name'],
    'Вес': pokemon_info['weight'],
    'Рост': pokemon_info['height'],
    'Способности': pokemon_info['abilities'][0]['ability']['name'],
}

print('\n'.join([f'{key}: {value}' for key, value in result.items()]))