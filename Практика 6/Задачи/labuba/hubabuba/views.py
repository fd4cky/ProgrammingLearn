"""
Django view functions for listing posts and showing book details.
"""
from django.shortcuts import render

# Create your views here.
def post_list(request):
    """
    Возвращает список книг с названием и обложкой.

    Parameters:
        request: HttpRequest — входящий HTTP‑запрос.

    Returns:
        HttpResponse — HTML‑страница со списком постов.
    """
    context = [
        {
            'title': 'Мастер и маргарита',
            'url': 'https://cdn.azbooka.ru/cv/w1100/fb79cabe-be6a-4a3e-804d-6209d66aa607.jpg',
        },
        {
            'title': 'Белая гвардия',
            'url': 'https://cdn.azbooka.ru/cv/w383/webp/058b015f-85dc-46f3-a052-b56d7d4ac612.webp',
        }
    ]

    return render(request, 'posts/post_list.html', {'posts': context})


def book_detail(request):
    """
    Возвращает подробную информацию о каждой книге.

    Parameters:
        request: HttpRequest — входящий HTTP‑запрос.

    Returns:
        HttpResponse — HTML‑страница с деталями книг.
    """
    context = [
        {
            'title': 'Мастер и маргарита',
            'author': 'Михаил Булгаков',
            'genre': 'Роман, мистика, философия',
            'content': '«Мастер и Маргарита» — одно из самых значительных произведений русской литературы XX века. Роман объединяет сатиру, любовную историю и философские размышления о добре, зле и свободе человека.',
        },
        {
            'title': 'Белая гвардия',
            'author': 'Михаил Булгаков',
            'genre': 'Роман, историческая проза',
            'content': '«Белая гвардия» — произведение Михаила Булгакова о судьбах интеллигенции и офицеров в годы Гражданской войны на Украине. Роман раскрывает тему верности, долга и поиска смысла жизни в эпоху потрясений.',
        }
    ]

    return render(request, 'book_detail.html', {'posts': context})