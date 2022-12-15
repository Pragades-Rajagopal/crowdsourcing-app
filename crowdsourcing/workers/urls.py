from django.urls import path
from . import views

app_name = 'workers'
urlpatterns = [
    path('', views.index, name='index'),
    path('searchaudio/', views.searchaudio, name='searchaudio'),
    path('getaudio/<int:audio_id>', views.getaudio, name='getaudio'),
    path('postdata/', views.postdata, name='postdata'),
    path('workers-data/', views.transcribe_data, name='workers-data'),
]
