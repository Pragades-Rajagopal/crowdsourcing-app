from django.shortcuts import render
from .models import Audios, Transcribe

def index(request):
    return render(request, 'workers/index.html')


