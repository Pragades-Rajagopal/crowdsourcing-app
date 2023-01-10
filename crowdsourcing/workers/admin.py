from django.contrib import admin
from .models import Audios

admin.site.site_header = 'Crowdsourcing application'
admin.site.site_title = 'App admin page'
admin.site.index_title = 'Welcome, Admin!'


class AudiosAdmin (admin.ModelAdmin):
    model = Audios


admin.site.register(Audios, AudiosAdmin)
