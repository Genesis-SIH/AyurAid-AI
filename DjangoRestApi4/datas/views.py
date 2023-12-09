from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from datas.models import Data
from datas.serializers import DataSerializer
from rest_framework.decorators import api_view


def index(request):
   return HttpResponse("<h1> App is running..</h1>")

@api_view(['GET', 'POST', 'DELETE'])
def data_list(request):
    if request.method == 'GET':
        datas = Data.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            datas = datas.filter(title__icontains=title)
        
        datas_serializer = DataSerializer(datas, many=True)
        return JsonResponse(datas_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        data_data = JSONParser().parse(request)
        data_serializer = DataSerializer(data=data_data)
        if data_serializer.is_valid():
            data_serializer.save()
            return JsonResponse(data_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Data.objects.all().delete()
        return JsonResponse({'message': '{} Data was deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def data_detail(request, pk):
    try: 
        data = Data.objects.get(pk=pk) 
    except Data.DoesNotExist: 
        return JsonResponse({'message': 'The data does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        data_serializer = DataSerializer(data) 
        return JsonResponse(data_serializer.data) 
 
    elif request.method == 'PUT': 
        data_data = JSONParser().parse(request) 
        data_serializer = DataSerializer(data, data=data_data) 
        if data_serializer.is_valid(): 
            data_serializer.save() 
            return JsonResponse(data_serializer.data) 
        return JsonResponse(data_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        data.delete() 
        return JsonResponse({'message': 'Data was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def data_list_published(request):
    datas = Data.objects.filter(published=True)
        
    if request.method == 'GET': 
        datas_serializer = DataSerializer(datas, many=True)
        return JsonResponse(datas_serializer.data, safe=False)