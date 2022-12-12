from django.contrib import admin
from .models import Audios

class AudiosAdmin (admin.ModelAdmin):
    model = Audios

admin.site.register(Audios, AudiosAdmin)
