from django.shortcuts import render
from django.http import HttpResponse
import time

from config.celery import app

@app.task
def mytask():
    time.sleep(10)
    open('namefile.txt' , 'w').close


# Create your views here.
def home(request):
    
    mytask.delay()
    
    return HttpResponse('Hello')    