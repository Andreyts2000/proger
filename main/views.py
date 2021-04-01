from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("<h4>Proverka rabotu</h4>")

def about(request):
	return HttpResponse("<h4>Stranica pro nas</h4>")
