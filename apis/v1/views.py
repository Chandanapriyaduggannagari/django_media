import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from app.models import book
from apis.v1.serializer import bookSerializers


@csrf_exempt
def all_books(request):
    if request.method == "GET":
        result=book.objects.all()
        serializedResult=bookSerializers(result,many=True)
        if serializedResult.is_valid:
            return JsonResponse(serializedResult.data,safe=False)
        else:
            return HttpResponse("some error occured")
    else:
        return HttpResponse("invaild")
    
@csrf_exempt
def add_book(request):
    if request.method == 'POST':
        incoming_data=JSONParser().parse(request)
        serializeData=bookSerializers(data = incoming_data)
        if serializeData.is_valid():
            serializeData.save()
            return JsonResponse(serializeData.data,status=201)
        return JsonResponse(serializeData.errors,status=400)
    return HttpResponse("invaild request method")


@csrf_exempt
def edit_book(request):
    if request.method == 'PATCH':
        incoming_data = JSONParser().parse(request)
        pk=incoming_data.get('id')
        obj=book.objects.get(id=pk)
        serializeData = bookSerializers(obj,data=incoming_data,partial=True)
        if serializeData.is_valid():
            serializeData.save()
            return JsonResponse(serializeData.data,status=201)
        return JsonResponse(serializeData.errors,status=400)
    return HttpResponse("invaild request method")


@csrf_exempt
def all_book(request):
    if request.method == 'PUT':
        incoming_data = JSONParser().parse(request)
        pk=incoming_data.get('id')
        obj=book.objects.get(id=pk)
        serializeData = bookSerializers(obj,data=incoming_data)
        if serializeData.is_valid():
            serializeData.save()
            return JsonResponse(serializeData.data,status=201)
        return JsonResponse(serializeData.errors,status=400)
    return HttpResponse("invaild request method")

@csrf_exempt
def delete_book(request):
    if request.method == 'DELETE':
        incoming_data = JSONParser().parse(request)
        pk=incoming_data.get('id')
        obj=book.objects.get(id=pk)
        obj.delete()
        return HttpResponse("delete successfully")
    
def only_one(request,auth):
    if request.method == "GET":
        result = book.objects.get(id=auth)
        obj= bookSerializers(result)
        if obj.is_valid:
            return JsonResponse(obj.data,status=201)
        else:
            return JsonResponse("error occured")
    return HttpResponse("invalid request")