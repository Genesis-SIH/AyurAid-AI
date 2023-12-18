# views.py
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from .serializers import YourSerializer
from .mongo import MongoDB
from datetime import datetime

class YourView(views.APIView):
    def post(self, request, *args, **kwargs):
        
        serializer = YourSerializer(data=request.data)
        print("Break 0")
        if serializer.is_valid():
            id = serializer.validated_data['id']
            text = serializer.validated_data['text']
            user_type = serializer.validated_data['type']
            timestamp = serializer.validated_data['timestamp']
            data = serializer.validated_data['data']
            print("Break 1")
            # Save to MongoDB
            mongo_client = MongoDB()
            mongo_client.collection.update_one(
                {"_id": id},
                {"$push": {"data": {"text": text, "type": user_type, "timestamp": timestamp, "data": data}}},
                upsert=True
            )
            mongo_client.close_connection()
            print("Break 2")
            # Response
            response_data = {
                "text": "Hello, This is Ayuraid.",
                "type": "bot",
                "timestamp":" datetime.now().isoformat()",
                "id":" datetime.now().timestamp()",
                "data": None,
            }
            print("Break 3")
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            print(serializer)
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


