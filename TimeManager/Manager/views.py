from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("TO JUZ W KROTCE BYNDZIE SUPER APKA DO ZARZADZANIA CZASEM ")
