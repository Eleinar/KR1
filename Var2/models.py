import django.db.models.deletion
from django.db import models


# Create your models here.
class Events(models.Model):
    event_id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=100, null=False, default='')
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    description = models.TextField(null=False, default='')


class Participants(models.Model):
    participant_id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=50, null=False, default='')
    info = models.TextField(null=False, default='')


class Participation_in_events(models.Model):
    participation_id = models.IntegerField(primary_key=True, null=False)
    event_id = models.ForeignKey('Events', on_delete=django.db.models.deletion.PROTECT)
    participant_id = models.ForeignKey('Participants', on_delete=django.db.models.deletion.PROTECT)
    role = models.CharField(max_length=20, null=False, default='')
