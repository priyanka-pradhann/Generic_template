from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def login(request):
    return render(request,'login.html')

def string_respones(request):
    return HttpResponse('this is string_respones')