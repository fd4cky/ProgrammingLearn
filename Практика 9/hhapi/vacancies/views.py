from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from .models import Vacancy
from .services import HHAPIService


def vacancy_list(request):
    # Показываем список всех вакансий с поиском и фильтрами
    vacancies = Vacancy.objects.all()
    
    # Поиск по названию, описанию, работодателю или городу
    search_query = request.GET.get('search', '')
    if search_query:
        vacancies = vacancies.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(employer_name__icontains=search_query) |
            Q(area_name__icontains=search_query)
        )
    
    # Фильтр по городу
    area_filter = request.GET.get('area', '')
    if area_filter:
        vacancies = vacancies.filter(area_name__icontains=area_filter)
    
    # Фильтр по опыту
    experience_filter = request.GET.get('experience', '')
    if experience_filter:
        vacancies = vacancies.filter(experience__icontains=experience_filter)
    
    # Фильтр по типу занятости
    employment_filter = request.GET.get('employment', '')
    if employment_filter:
        vacancies = vacancies.filter(employment__icontains=employment_filter)
    
    # Фильтр по графику
    schedule_filter = request.GET.get('schedule', '')
    if schedule_filter:
        vacancies = vacancies.filter(schedule__icontains=schedule_filter)
    
    # Фильтр по категории профессии
    professional_role_filter = request.GET.get('professional_role', '')
    if professional_role_filter:
        vacancies = vacancies.filter(professional_role__icontains=professional_role_filter)
    
    # Фильтр по зарплате
    salary_filter = request.GET.get('salary', '')
    if salary_filter:
        try:
            min_salary = int(salary_filter)
            vacancies = vacancies.filter(
                Q(salary_from__gte=min_salary) | Q(salary_to__gte=min_salary)
            )
        except:
            pass
    
    # Разбиваем на страницы по 20 вакансий
    paginator = Paginator(vacancies, 20)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    # Получаем списки для выпадающих фильтров
    areas = Vacancy.objects.values_list('area_name', flat=True).distinct().exclude(area_name='').order_by('area_name')
    experiences = Vacancy.objects.values_list('experience', flat=True).distinct().exclude(experience='').order_by('experience')
    employments = Vacancy.objects.values_list('employment', flat=True).distinct().exclude(employment='').order_by('employment')
    schedules = Vacancy.objects.values_list('schedule', flat=True).distinct().exclude(schedule='').order_by('schedule')
    professional_roles = Vacancy.objects.values_list('professional_role', flat=True).distinct().exclude(professional_role='').order_by('professional_role')
    
    context = {
        'page_obj': page_obj,
        'vacancies': page_obj,
        'search_query': search_query,
        'area_filter': area_filter,
        'experience_filter': experience_filter,
        'employment_filter': employment_filter,
        'schedule_filter': schedule_filter,
        'professional_role_filter': professional_role_filter,
        'salary_filter': salary_filter,
        'areas': areas,
        'experiences': experiences,
        'employments': employments,
        'schedules': schedules,
        'professional_roles': professional_roles,
        'total_count': paginator.count,
    }
    
    return render(request, 'vacancies/vacancy_list.html', context)


def vacancy_detail(request, vacancy_id):
    # Показываем детальную информацию о вакансии
    vacancy = get_object_or_404(Vacancy, id=vacancy_id)
    
    context = {
        'vacancy': vacancy,
    }
    
    return render(request, 'vacancies/vacancy_detail.html', context)


def fetch_vacancies(request):
    # Загружаем вакансии из HH API
    if request.method == 'POST':
        search_text = request.POST.get('search_text', '')
        area = int(request.POST.get('area', 1))  # по умолчанию Москва
        per_page = int(request.POST.get('per_page', 50))
        
        # Собираем фильтры
        experience = request.POST.get('experience', '')
        employment = request.POST.get('employment', '')
        schedule = request.POST.get('schedule', '')
        salary = request.POST.get('salary', '')
        
        filters = {}
        if experience:
            filters['experience'] = experience
        if employment:
            filters['employment'] = employment
        if schedule:
            filters['schedule'] = schedule
        if salary:
            try:
                filters['salary'] = int(salary)
            except:
                pass
        
        try:
            saved_count = HHAPIService.fetch_and_save_vacancies(
                search_text=search_text,
                area=area,
                per_page=per_page,
                **filters
            )
            messages.success(request, f'Успешно сохранено {saved_count} вакансий!')
        except Exception as e:
            messages.error(request, f'Ошибка при получении вакансий: {str(e)}')
        
        return redirect('vacancies:vacancy_list')
    
    # Показываем форму для загрузки
    context = {
        'areas': [
            {'id': 1, 'name': 'Москва'},
            {'id': 2, 'name': 'Санкт-Петербург'},
            {'id': 3, 'name': 'Екатеринбург'},
            {'id': 4, 'name': 'Новосибирск'},
            {'id': 88, 'name': 'Казань'},
            {'id': 66, 'name': 'Нижний Новгород'},
        ],
        'experiences': [
            {'value': 'noExperience', 'name': 'Нет опыта'},
            {'value': 'between1And3', 'name': 'От 1 года до 3 лет'},
            {'value': 'between3And6', 'name': 'От 3 до 6 лет'},
            {'value': 'moreThan6', 'name': 'Более 6 лет'},
        ],
        'employments': [
            {'value': 'full', 'name': 'Полная занятость'},
            {'value': 'part', 'name': 'Частичная занятость'},
            {'value': 'project', 'name': 'Проектная работа'},
            {'value': 'volunteer', 'name': 'Волонтерство'},
            {'value': 'probation', 'name': 'Стажировка'},
        ],
        'schedules': [
            {'value': 'fullDay', 'name': 'Полный день'},
            {'value': 'shift', 'name': 'Сменный график'},
            {'value': 'flexible', 'name': 'Гибкий график'},
            {'value': 'remote', 'name': 'Удаленная работа'},
            {'value': 'flyInFlyOut', 'name': 'Вахтовый метод'},
        ],
    }
    
    return render(request, 'vacancies/fetch_vacancies.html', context)
