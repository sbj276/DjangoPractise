from django.views.generic import TemplateView

class HomePageView(TemplateView):
	template_name = 'home.html'
class AboutPageView(TemplateView):
	template_name = 'about.html'
# from django.shortcuts import render
# from django.http import HttpResponse

# def homePageView(request):
# 	return HttpResponse('<h1>Hello, Sachin</h1>')
# # Create your views here.
