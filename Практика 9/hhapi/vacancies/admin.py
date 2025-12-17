from django.contrib import admin
from .models import Vacancy


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    # Настройки админки для вакансий
    list_display = ('name', 'employer_name', 'professional_role', 'area_name', 'salary_from', 'salary_to', 'published_at')
    list_filter = ('area_name', 'professional_role', 'experience', 'employment', 'schedule', 'published_at')
    search_fields = ('name', 'description', 'employer_name', 'area_name', 'professional_role')
    readonly_fields = ('hh_id', 'created_at', 'updated_at')
    fieldsets = (
        ('Основная информация', {
            'fields': ('hh_id', 'name', 'description', 'url')
        }),
        ('Зарплата', {
            'fields': ('salary_from', 'salary_to', 'salary_currency')
        }),
        ('Работодатель', {
            'fields': ('employer_name', 'employer_id', 'employer_logo_url')
        }),
        ('Локация', {
            'fields': ('area_name', 'area_id')
        }),
        ('Условия работы', {
            'fields': ('professional_role', 'experience', 'schedule', 'employment')
        }),
        ('Детали', {
            'fields': ('requirement', 'responsibility')
        }),
        ('Даты', {
            'fields': ('published_at', 'created_at', 'updated_at')
        }),
    )
