from django.urls import path
from . import views

app_name = 'vacancies'

# URL маршруты для приложения
urlpatterns = [
    path('', views.vacancy_list, name='vacancy_list'),  # Список вакансий
    path('fetch/', views.fetch_vacancies, name='fetch_vacancies'),  # Загрузка вакансий
    path('<int:vacancy_id>/', views.vacancy_detail, name='vacancy_detail'),  # Детали вакансии
]

