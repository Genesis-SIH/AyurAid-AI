from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from .serializers import YourSerializer

class YourView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = YourSerializer(data=request.data)

        if serializer.is_valid():
          
            answer = "This is a dummy answer."
            source = "Dummy source data."
            data = {"key": "value"}  

            response_data = {
                "answer": answer,
                "source": source,
                "data": data,
            }

            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
