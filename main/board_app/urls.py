from django.urls import path
from . import views
app_name = 'boards'
urlpatterns = [
  path('', views.index,name='index'),
  path('<int:pk>/all', views.board_topics_all,name='topics_all'),
  path('<int:pk>/all', views.board_topics_new,name='topics_new'),
]