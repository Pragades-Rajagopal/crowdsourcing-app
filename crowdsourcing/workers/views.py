from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from .models import Audios, Transcribe
import datetime
from pathlib import Path
import os
import csv

BASE_DIR = Path(__file__).resolve().parent.parent
EXPORT_PATH = os.path.join(BASE_DIR, 'exports')


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


def getaudio(request, audio_id):
    audio = get_object_or_404(Audios, pk=audio_id)
    return render(request, 'workers/getaudio.html', {'audio_data': audio})


def postdata(request):
    username = request.POST.get('username')
    data = request.POST.get('trans_data')
    audio_id = request.POST.get('audio_id')
    current_time = datetime.datetime.now()
    inputs = Transcribe(username=username, data=data,
                        created_at=current_time, audio_id=audio_id)
    inputs.save()
    sample_transcribed_data = Transcribe.objects.filter(
        audio_id=audio_id).order_by('-id')[1:10]
    return render(request, 'workers/thanks.html', {'data': sample_transcribed_data, 'input': data, 'trans_id': inputs.id})


def postnextdata(request):
    id = request.POST.get('trans_id')
    data = request.POST.get('trans_data2')
    t = Transcribe.objects.get(pk=id)
    t.data2 = data
    t.save()
    return render(request, 'workers/final.html')


def transcribe_data(request):
    data = Transcribe.objects.all()
    results = []
    for i in range(0, data.count()):
        audio_name = Audios.objects.get(pk=data[i].audio_id)
        results.append({'audio_name': audio_name, 'data': data[i]})
    return render(request, 'workers/worker-data.html', {'results': results})


def exportData(request):
    data = Transcribe.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=export.csv'
    writer = csv.writer(response)
    writer.writerow(['Username', 'Transcribed data',
                    'Transcribed data after', 'Created at'])
    tdata = data.values_list('username', 'data', 'data2',
                             'created_at')
    for t in tdata:
        writer.writerow(t)
    return response
