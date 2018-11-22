from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User 
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.

class Answer_Options(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Answer Option"
        verbose_name_plural = "Answer Options"

class Quiz(models.Model):
    quiz_name = models.CharField(max_length=200)

    def __str__(self):
        return self.quiz_name

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizes"

class Topic(models.Model):
    IMPORTANCE_SCORE = (
    ('LOW','Low'),
    ('NORMAL', 'Normal'),
    ('HIGH','High'),
    )
    topic_name = models.CharField(max_length=200)
    importance_score = models.CharField(max_length=6, choices= IMPORTANCE_SCORE, default='LOW')
    complexity_score = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.topic_name
    
    class Meta:
        verbose_name = "Topic"
        verbose_name_plural = "Topics"

class Sub_Topic(models.Model):
    IMPORTANCE_SCORE = (
    ('LOW','Low'),
    ('NORMAL', 'Normal'),
    ('HIGH','High'),
    )
    subtopic_name = models.CharField(max_length=200)
    importance_score = models.CharField(max_length=6, choices= IMPORTANCE_SCORE, default='LOW')
    complexity_score = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.subtopic_name
    
    class Meta:
        verbose_name = "Sub Topic"
        verbose_name_plural = "Sub Topics"

class Quiz_Question(models.Model):
    STATUS_CHOICES = ( 
        ('draft', 'Draft'), 
        ('published', 'Published'), 
    ) 
    subject = models.ForeignKey(Quiz, on_delete=models.CASCADE, blank=True, default=None, null=True)
    title = models.CharField(max_length=250) 
    slug = models.SlugField(max_length=250,  
                            unique_for_date='publish') 
    main_topic = models.ForeignKey(Topic,on_delete=models.CASCADE, blank=True, default=None, null=True)
    sub_topic = models.ForeignKey(Sub_Topic,on_delete=models.CASCADE, blank=True, default=None, null=True)
    #q_type = models.CharField(max_length=50)
    publish = models.DateTimeField(default=timezone.now) 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    status = models.CharField(max_length=10,  
                              choices=STATUS_CHOICES, 
                              default='draft') 
    text = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    possible_answers = models.ManyToManyField(Answer_Options)
    #selected = models.ForeignKey(Answer_Options, related_name="selected", default=None, on_delete=models.CASCADE, blank=True, null=True)
    correct = models.ForeignKey(Answer_Options, related_name="correct", default=None, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Quiz Question"
        verbose_name_plural = "Quiz Questions"

