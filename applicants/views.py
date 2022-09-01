from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import Candidato
from .serializers import AppSerializer

@api_view(['GET', 'POST', 'DELETE'])
def getAdd(request):
  if request.method == 'GET':
    applicants = Candidato.objects.all()
    app_serializer = AppSerializer(applicants, many=True)
    return JsonResponse(app_serializer.data, safe=False)

  elif request.method == 'POST':
    applicant_data = JSONParser().parse(request)
    app_serializer = AppSerializer(data=applicant_data)
    if app_serializer.is_valid():
      app_serializer.save()
      return JsonResponse(app_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(app_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    applicants = Candidato.objects.all()
    applicants.delete()
    return JsonResponse({'message': 'Candidatos deletados com sucesso.'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def getUpdateDelete(request, id):
  try:
    applicant = Candidato.objects.get(pk=id)
  except Candidato.DoesNotExist():
    return JsonResponse({'message': 'Esse candidato não existe.'}, status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    app_serializer = AppSerializer(applicant)
    return JsonResponse(app_serializer.data)

  elif request.method == 'PUT':
    applicant_data = JSONParser().parse(request)
    app_serializer = AppSerializer(applicant, data=applicant_data)
    if app_serializer.is_valid():
      app_serializer.save()
      return JsonResponse(app_serializer.data)
    return JsonResponse(app_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    applicant.delete()
    return JsonResponse({'message': 'Candidato deletado com sucesso.'}, status=status.HTTP_204_NO_CONTENT)


