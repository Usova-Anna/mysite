from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(response):
	return HttpResponse("<h1>Hey you!</h1>")

def view1(response):
	return HttpResponse("<h1>Ok, bye! It was view1<h1>")