from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from django.http.request import HttpRequest
from django.http.response import HttpResponse

import json
from django.shortcuts import render

from django.http.response import JsonResponse

from api.serializer import CompanySerializer, VacancySerializer, ProductsSerializer, PeopleSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from api.models import Company,Vacancy, People, Products

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def company_list(request):

    if request.method == "GET":
        permission_classes = [IsAuthenticated]
        companies = Company.objects.all()
        #companies_json = [company.to_json() for company in companies]
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET','PUT', 'DELETE'])
def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)
    if request.method == "GET":
        serializer = CompanySerializer(company)
        return Response(serializer.data)
    elif request.method == "PUT":

        serializer = CompanySerializer(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == "DELETE":
        company.delete()
        return Response({'message': "deleted"}, status=204)

@api_view(['GET'])
def com_vac(request, company_id):
    company = Vacancy.objects.all().filter(company=company_id)
    compan_json = [compan.to_json() for compan in company]
    return JsonResponse(compan_json, safe=False)

@api_view(['GET', 'POST'])
def vacancies_show(request):

    if request.method == "GET":
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        #vacancies_json = [vacancy.to_json() for vacancy in vacancies]
        return Response(serializer.data)
    elif request.method == "POST":

        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def vacancies_detail(request, vac_id):
    try:
        vac = Vacancy.objects.get(id=vac_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)
    if request.method == "GET":
        serializer = VacancySerializer(vac)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = VacancySerializer(instance=vac, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == "DELETE":
        vac.delete()
        return Response({'message': "deleted"}, status=204)

@api_view(['GET', 'POST'])
def people_list(request):
    if request.method == "GET":
        peoples = People.objects.all()
        #companies_json = [company.to_json() for company in companies]
        serializer = PeopleSerializer(peoples, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = json.loads(request.body)
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
@api_view(['GET'])
def people_detail(request, people_id):
    try:
        peoples = People.objects.get(id=people_id)
    except People.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)
    if request.method == "GET":
        serializer = PeopleSerializer(peoples)
        return JsonResponse(serializer.data)
@api_view(['GET'])
def products_list(request):
    if request.method == "GET":
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        #vacancies_json = [vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def people_products(request, people_id):
    person = Products.objects.all().filter(person=people_id)
    compan_json = [pr.to_json() for pr in person]
    return JsonResponse(compan_json, safe=False)
@api_view(['GET'])
def products_detail(request, products_id):
    try:
        products = Products.objects.get(id=products_id)
    except Products.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)
    if request.method == "GET":
        serializer = ProductsSerializer(products)
        return JsonResponse(serializer.data)
