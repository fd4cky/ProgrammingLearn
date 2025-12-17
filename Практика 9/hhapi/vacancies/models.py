from django.db import models
from django.utils import timezone


class Vacancy(models.Model):
    # Модель для хранения вакансий из HeadHunter
    hh_id = models.CharField(max_length=20, unique=True, verbose_name="ID в HH")
    name = models.CharField(max_length=500, verbose_name="Название вакансии")
    description = models.TextField(blank=True, verbose_name="Описание")
    salary_from = models.IntegerField(null=True, blank=True, verbose_name="Зарплата от")
    salary_to = models.IntegerField(null=True, blank=True, verbose_name="Зарплата до")
    salary_currency = models.CharField(max_length=10, blank=True, verbose_name="Валюта")
    employer_name = models.CharField(max_length=300, blank=True, verbose_name="Работодатель")
    employer_id = models.CharField(max_length=20, blank=True, verbose_name="ID работодателя")
    employer_logo_url = models.URLField(blank=True, verbose_name="Логотип работодателя")
    area_name = models.CharField(max_length=200, blank=True, verbose_name="Город")
    area_id = models.CharField(max_length=20, blank=True, verbose_name="ID города")
    experience = models.CharField(max_length=100, blank=True, verbose_name="Опыт работы")
    schedule = models.CharField(max_length=100, blank=True, verbose_name="График работы")
    employment = models.CharField(max_length=100, blank=True, verbose_name="Тип занятости")
    published_at = models.DateTimeField(null=True, blank=True, verbose_name="Дата публикации")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания записи")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    url = models.URLField(blank=True, verbose_name="Ссылка на вакансию")
    requirement = models.TextField(blank=True, verbose_name="Требования")
    responsibility = models.TextField(blank=True, verbose_name="Обязанности")
    professional_role = models.CharField(max_length=200, blank=True, verbose_name="Категория профессии")
    
    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"
        ordering = ['-published_at', '-created_at']
        indexes = [
            models.Index(fields=['hh_id']),
            models.Index(fields=['name']),
            models.Index(fields=['area_name']),
            models.Index(fields=['professional_role']),
        ]
    
    def __str__(self):
        return f"{self.name} - {self.employer_name}"
