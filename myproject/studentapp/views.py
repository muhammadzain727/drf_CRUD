from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .serializers import Student_data_serializer
from rest_framework.decorators import api_view
from .models import StudentData
# Create your views here.
@api_view(['GET'])
def read(request):
    if request.method == 'GET':
        queryset = StudentData.objects.all()
        serializer = Student_data_serializer(queryset, many=True)
        return JsonResponse(serializer.data,safe=False)


@api_view(['POST'])
def create(request):
    if request.method=="POST":
        print('================', request.data)
        serializer=Student_data_serializer(data=request.data) 
        if serializer.is_valid():
            
            serializer.save()
            print('=======', serializer.data)
            res= {'msg':'Data Created'}
            return HttpResponse(res)
        return HttpResponse({'error': serializer.errors})  
    

@api_view(['PUT'])
def update(request,id):
    if request.method=="PUT":  
        instance = StudentData.objects.get(pk=id)       
        serializer=Student_data_serializer(instance,data=request.data) 
        if serializer.is_valid():
            serializer.save()
            res= {'msg':'Data Updated'}
            return HttpResponse(res)
        return HttpResponse({'error': serializer.errors}) 
    

@api_view(['DELETE'])
def delete(request,id):
    if request.method=="DELETE":  
        instance = StudentData.objects.get(pk=id) 
        instance.delete()      
        res= {'msg':'Data Deleted'}

        return HttpResponse(res)
        