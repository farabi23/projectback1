from django.contrib import admin
from api.models import Company, Vacancy, People, Products
# Register your models here.

admin.site.register(Company)
admin.site.register(Vacancy)
admin.site.register(People)
admin.site.register(Products)