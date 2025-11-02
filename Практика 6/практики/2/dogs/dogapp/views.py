from django.shortcuts import render
import requests


def main(request):
    items = []
    breeds = []
    if request.method == "POST":
        # Получаем строку с породами из формы, убираем пробелы по краям и разбиваем по запятой с пробелом
        # strip() нужен, чтобы убрать лишние пробелы в начале и конце строки
        # разделение через ', ' предполагает, что пользователь вводит породы через запятую и пробел
        raw = request.POST.get("query", "").strip()
        if raw:
            breeds = [p for p in raw.split(', ') if p]

    # Для каждой породы делаем запрос к API, чтобы получить изображение
    # Проверяем, что ответ успешный (код 200), иначе считаем, что порода не найдена
    for breed in breeds:
        response = requests.get(
            f'https://dog.ceo/api/breed/{breed}/images'
        )
        if response.status_code == 200:
            items.append([breed, response.json()['message'][0]])
        else:
            # Если порода не найдена, добавляем в список специальную пару с сообщением и картинкой ошибки
            items.append([
                'Порода не найдена',
                'https://blog.capdata.fr/wp-content/uploads/2023/09/code_erreur.jpeg'
            ])

    return render(request, "main.html", {"items": items})


def dogs_list(request):
    response = requests.get('https://dog.ceo/api/breeds/list/all').json()
    # API возвращает JSON вида {"message": {"breed1": [...], "breed2": [...]}, "status": "success"}
    # Берём только названия пород (ключи)
    result = [breed for breed in response['message']]
    return render(request, "dogs_list.html", {"items": result})