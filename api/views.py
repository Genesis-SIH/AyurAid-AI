from rest_framework import generics
from .models import Prompt
from .serializers import PromptSerializer

class PromptAPIView(generics.CreateAPIView):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer
