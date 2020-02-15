from rest_framework import serializers
from qa.models import Question, Answer, User

class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['title', 'text', 'added_at', 'rating', 'author', 'likes']

class AnswerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['text', 'added_at', 'question', 'author']