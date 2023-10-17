from django.shortcuts import render, redirect
import pyqrcode
import png
from pyqrcode import QRCode
from django.contrib import messages
# Create your views here.


def home(request):


    
    return render(request, 'home.html',)


def qrmaker(request):
    
    if request.method == "GET":

        urls = request.GET['url']
        names = request.GET['save']
        messages.success(request, 'Your qrcode image has been saved on your device')
    else:
        return redirect('home')

    QRstring = urls
    url = pyqrcode.create(QRstring)
    url.png(names, scale=8)

    context = {

    }

    return render(request, 'result.html', context=context)
