from rest_framework import generics
from .models import Question, Answer
from .serializers import *

class QuestionListView(generics.ListAPIView):
    serializer_class = QuestionListSerializer
    queryset = Question.objects.all()

class QuestionCreateView(generics.CreateAPIView):
    serializer_class = QuestionCreateSerializer