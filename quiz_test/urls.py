from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.quiz_home, name='quiz_home'),
    path('add/', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
]