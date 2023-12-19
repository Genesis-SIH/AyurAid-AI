# views.py
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from .serializers import YourSerializer
import api.mongoClient as mongoClient
from datetime import datetime


class YourView(views.APIView):
    def post(self, request, *args, **kwargs):
        
        serializer = YourSerializer(data=request.data)

        if serializer.is_valid():
            id = serializer.validated_data['id']
            text = serializer.validated_data['text']
            user_type = serializer.validated_data['type']
            timestamp = serializer.validated_data['timestamp']
            data = serializer.validated_data['data']

            response_data = {
                'id': id,
                'text': text,
                'type': user_type,
                'timestamp': timestamp,
                'data': data
            }

            mongoClient.colChats.insert_one(response_data)
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            print(serializer)
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


