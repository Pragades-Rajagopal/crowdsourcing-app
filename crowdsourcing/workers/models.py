from django.db import models

class Audios (models.Model):
    audio_name = models.CharField(max_length=200)
    audio_file = models.FileField(upload_to='audio/')
    tag = models.CharField(max_length=50)

    class Meta:
        db_table = 'Audio_table'

    def __str__(self):
        return self.audio_name

class Transcribe (models.Model):
    username = models.CharField(max_length=100)
    data = models.CharField(max_length=100000)
    created_at = models.DateField()
    audio = models.ForeignKey(Audios, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' %(self.username, self.created_at)    


