from django.shortcuts import render

# Create your views here.
from multiprocessing import context
from pickle import TRUE
from unittest import result
from django.shortcuts import render
import cv2
import threading
# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.core.mail import EmailMessage
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
from multiprocessing import Process
from polls.app import Application
from polls.number_app import Application1



def innerpg(request):
    return render(request, 'innerpg.html')


def new(reqest):
    return render(reqest,'new.html')

def appStart(request):
    pba = Application()
    pba.root.mainloop()
    return render(request, 'innerpg.html')

def appStart1(request):
    pba = Application1()
    pba.root.mainloop()
    return render(request, 'innerpg.html')