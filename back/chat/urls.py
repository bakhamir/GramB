from django.urls import path
from .views import MessageList

urlpatterns = [
    path('api/messages/', MessageList.as_view()),
]
