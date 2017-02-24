#Librerias
from django.shortcuts import render
from django.shortcuts import HttpResponse


#def index(request):
#	return render(request,"index.html")

class Entry():
	def  __init__(self,title,body,img_url):
		self.title = title
		self.body = body
                self.img_url = img_url


def index(request):
	entrys = [
		Entry("1er Post","1era Linea","http://static.notinerd.com/wp-content/uploads/2015/09/4105.jpg"),
		Entry("2do Post","2da Linea","http://static.notinerd.com/wp-content/uploads/2015/09/4105.jpg")
	]
	entrys_total = len(entrys)
	return render(request,"index.html",{'entrys':entrys,'entrys_total':entrys_total})

