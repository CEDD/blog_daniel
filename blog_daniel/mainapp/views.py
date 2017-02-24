#Librerias
from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Entry

def index(request):
	entrys = Entry.objects.all()
	entrys_total = len(entrys)
	
	return render(request,"index.html",{'entrys':entrys,'entrys_total':entrys_total})

