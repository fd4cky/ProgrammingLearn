# Сервис для работы с API HeadHunter
import requests
from datetime import datetime
from django.utils import timezone
from .models import Vacancy


class HHAPIService:
    # Класс для работы с API HeadHunter
    
    BASE_URL = "https://api.hh.ru"
    
    @staticmethod
    def get_vacancies(search_text="", area=1, per_page=100, 
                     experience=None, employment=None, 
                     schedule=None, salary=None):
        # Получаем список вакансий из API
        url = f"{HHAPIService.BASE_URL}/vacancies"
        params = {
            "text": search_text,
            "area": area,
            "per_page": min(per_page, 100),  # максимум 100
            "page": 0,
        }
        
        # Добавляем фильтры если они есть
        if experience:
            params["experience"] = experience
        if employment:
            params["employment"] = employment
        if schedule:
            params["schedule"] = schedule
        if salary:
            params["salary"] = salary
        
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Ошибка при запросе к HH API: {e}")
            return {"items": [], "found": 0, "pages": 0}
    
    @staticmethod
    def get_vacancy_detail(vacancy_id):
        # Получаем детальную информацию о вакансии по ID
        url = f"{HHAPIService.BASE_URL}/vacancies/{vacancy_id}"
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Ошибка при получении деталей вакансии: {e}")
            return None
    
    @staticmethod
    def parse_salary(salary_data):
        # Парсим данные о зарплате
        if not salary_data:
            return None, None, ""
        
        salary_from = salary_data.get("from")
        salary_to = salary_data.get("to")
        currency = salary_data.get("currency", "")
        return salary_from, salary_to, currency
    
    @staticmethod
    def parse_experience(experience_data):
        # Парсим опыт работы
        if not experience_data:
            return ""
        return experience_data.get("name", "")
    
    @staticmethod
    def parse_schedule(schedule_data):
        # Парсим график работы
        if not schedule_data:
            return ""
        return schedule_data.get("name", "")
    
    @staticmethod
    def parse_employment(employment_data):
        # Парсим тип занятости
        if not employment_data:
            return ""
        return employment_data.get("name", "")
    
    @staticmethod
    def save_vacancy_from_api(vacancy_data):
        # Сохраняем вакансию в базу данных
        hh_id = str(vacancy_data.get("id", ""))
        
        # Проверяем есть ли уже такая вакансия
        vacancy, created = Vacancy.objects.get_or_create(
            hh_id=hh_id,
            defaults={
                "name": vacancy_data.get("name", ""),
                "description": vacancy_data.get("description", ""),
                "url": vacancy_data.get("alternate_url", ""),
                "requirement": vacancy_data.get("snippet", {}).get("requirement", ""),
                "responsibility": vacancy_data.get("snippet", {}).get("responsibility", ""),
            }
        )
        
        # Заполняем данные о зарплате
        salary_from, salary_to, currency = HHAPIService.parse_salary(vacancy_data.get("salary"))
        vacancy.salary_from = salary_from
        vacancy.salary_to = salary_to
        vacancy.salary_currency = currency
        
        # Информация о работодателе
        employer = vacancy_data.get("employer", {})
        vacancy.employer_name = employer.get("name", "")
        vacancy.employer_id = str(employer.get("id", ""))
        
        # Логотип компании
        logo_urls = employer.get("logo_urls", {})
        if logo_urls:
            # Берем оригинальный размер или 90x90
            vacancy.employer_logo_url = logo_urls.get("original") or logo_urls.get("90x90") or ""
        
        # Категория профессии
        professional_roles = vacancy_data.get("professional_roles", [])
        if professional_roles:
            vacancy.professional_role = professional_roles[0].get("name", "")
        
        # Город
        area = vacancy_data.get("area", {})
        vacancy.area_name = area.get("name", "")
        vacancy.area_id = str(area.get("id", ""))
        
        # Опыт, график, занятость
        vacancy.experience = HHAPIService.parse_experience(vacancy_data.get("experience"))
        vacancy.schedule = HHAPIService.parse_schedule(vacancy_data.get("schedule"))
        vacancy.employment = HHAPIService.parse_employment(vacancy_data.get("employment"))
        
        # Дата публикации
        published_str = vacancy_data.get("published_at")
        if published_str:
            try:
                # Конвертируем дату из формата HH API
                if published_str.endswith('Z'):
                    published_str = published_str.replace('Z', '+00:00')
                elif len(published_str) > 19:
                    # Преобразуем +0300 в +03:00
                    if published_str[-5] in ['+', '-']:
                        tz_sign = published_str[-5]
                        tz_hours = published_str[-4:-2]
                        tz_mins = published_str[-2:]
                        published_str = published_str[:-5] + f"{tz_sign}{tz_hours}:{tz_mins}"
                
                published_at = datetime.fromisoformat(published_str)
                if timezone.is_naive(published_at):
                    published_at = timezone.make_aware(published_at)
                vacancy.published_at = published_at
            except Exception as e:
                # Если не получилось распарсить дату - пропускаем
                print(f"Ошибка парсинга даты: {e}")
                pass
        
        vacancy.save()
        return vacancy
    
    @staticmethod
    def fetch_and_save_vacancies(search_text="", area=1, per_page=100, **filters):
        # Получаем вакансии из API и сохраняем в БД
        data = HHAPIService.get_vacancies(
            search_text=search_text,
            area=area,
            per_page=per_page,
            **filters
        )
        
        saved_count = 0
        items = data.get("items", [])
        
        # Проходим по каждой вакансии и сохраняем
        for item in items:
            try:
                # Получаем полную информацию о вакансии по ID
                vacancy_id = item.get("id")
                detail = HHAPIService.get_vacancy_detail(vacancy_id)
                if detail:
                    HHAPIService.save_vacancy_from_api(detail)
                    saved_count = saved_count + 1
            except Exception as e:
                print(f"Ошибка при сохранении вакансии: {e}")
                continue
        
        return saved_count

