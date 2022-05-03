"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
);



#from api.views.serializers_1 import company_list, company_detail, com_vac, vacancies_show, vacancies_detail, people_list, people_detail, products_list, people_products, products_detail
from api.views.fbv_view import company_list, company_detail, com_vac, vacancies_show, vacancies_detail, products_detail, products_list, people_products, people_detail, people_list
#from api.views.cbv_view import CompanyDetailAPIView, CompanyListAPIView, VacancyDetailAPIView, VacancyListAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/companies', company_list),
    path('api/companies/<int:company_id>/', company_detail),
    path('api/companies/<int:company_id>/vacancies/', com_vac),
    path('api/vacancies/', vacancies_show),
    path('api/vacancies/<int:vac_id>/', vacancies_detail),
    path('api/people', people_list),
    path('api/people/<int:people_id>/', people_detail),
    path('api/people/<int:people_id>/products', people_products),
    path('api/products', products_list),
    path('api/products/<int:products_id>', products_detail),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair' ),

]


'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/companies', CompanyListAPIView.as_view()),
    path('api/companies/<int:pk>/', CompanyDetailAPIView.as_view()),
    path('api/vacancies/', VacancyListAPIView.as_view()),
    path('api/vacancies/<int:pk>/', VacancyDetailAPIView.as_view()),

]
'''
