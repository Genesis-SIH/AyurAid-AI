from django.urls import path
from .views import YourView

urlpatterns = [
    path('chatbot/ask/', YourView.as_view(), name='chatbot_ask'),
]


