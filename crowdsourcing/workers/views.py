from django.shortcuts import render
from django.http import Http404
from .models import Audios, Transcribe


def index(request):
    audio_tags = Audios.objects.all().values('tag').distinct()
    print(audio_tags)
    values = []
    for i in range(0, audio_tags.count()):
        values.append({'tags': audio_tags[i]['tag']})
    print('values --', values)
    return render(request, 'workers/index.html', {'audio_tags': values})


def searchaudio(request):
    audio_tag = request.POST.get('audio_tag')
    try:
        audio_data = Audios.objects.filter(tag=audio_tag)
    except (KeyError, Audios.DoesNotExist):
        raise Http404('Audios not available for the given audio tag')

    return render(request, 'workers/searchaudio.html', {'audio_data': audio_data})
