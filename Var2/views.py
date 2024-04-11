from django.shortcuts import render
import sqlite3
from .models import Events, Participants
# Create your views here.
def index(request):
    events = Events.objects.all()
    participants = Participants.objects.all()
    return render(request, 'index.html', {'events' : events, 'participants': participants})