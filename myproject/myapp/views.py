from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # context = {
    #     'name':'Aryan',
    #     'age':18,
    #     'city':'Jaipur'
    # }
    #return render(request , 'index.html')
    return render(request , 'index.html')

def counter(request):
    text  = request.POST['text']
    number_of_words = len(text.split())
    return render(request , 'counter.html' , {'count':number_of_words})