from .models import *
from rest_framework import viewsets
from .serializers import *

class Answer_OptionsViewSet(viewsets.ModelViewSet):
    queryset = Answer_Options.objects.all()
    serializer_class = Answer_OptionsSerializer

    
class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer  
    
class Sub_TopicViewSet(viewsets.ModelViewSet):
    queryset = Sub_Topic.objects.all()
    serializer_class = Sub_TopicSerializer

class Quiz_QuestionViewSet(viewsets.ModelViewSet):
    queryset = Quiz_Question.objects.all()
    serializer_class = Quiz_QuestionSerializer