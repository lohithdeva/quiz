from .models import *
from rest_framework import serializers

class Answer_OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer_Options
        fields = ('url', 'text')

class QuizSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quiz
        fields = ('url', 'quiz_name')

class TopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topic
        fields = ('url', 'topic_name')

class Sub_TopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sub_Topic
        fields = ('url', 'subtopic_name')
        
class Quiz_QuestionSerializer(serializers.HyperlinkedModelSerializer):
    possible_answers = Answer_OptionsSerializer(many=True, read_only=True)
    correct = Answer_OptionsSerializer(read_only=True)
    class Meta:
        model = Quiz_Question
        fields = ('url', 'subject', 'title','slug','main_topic','sub_topic', 
                    'publish','created','updated','status','text','possible_answers','correct')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('author')