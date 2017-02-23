#Librerias
from django.shortcuts import render
from django.shortcuts import HttpResponse


#def index(request):
#	return render(request,"index.html")

class Entry():
	def  __init__(self,title,body):
		self.title = title
		self.body = body

def index(request):
	entrys = [
		Entry("1er Post","1era Linea"),
		Entry("2do Post","2da Linea")
	]
	entrys_total = len(entrys)
	return render(request,"index.html",{'entrys':entrys,'entrys_total':entrys_total})

