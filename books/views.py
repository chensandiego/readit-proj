from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.
def list_books(request):
	return HttpResponse('we could put anything here')