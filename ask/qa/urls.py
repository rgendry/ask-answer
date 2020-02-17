from django.urls import path
from .views import *

urlpatterns = [
    path('', QuestionListView.as_view()),
    path('ask/', QuestionCreateView.as_view()),
]