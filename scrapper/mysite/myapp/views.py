from django.shortcuts import render
from django.http import HttpResponseRedirect
from bs4 import BeautifulSoup
from .models import Link
import requests
# Create your views here.

def scrape(request):
    if request.method == "POST":
        site = request.POST.get('site','')
        if(site=='' or site is None):
            site='https://www.google.com'
        page = requests.get(site)
        soup = BeautifulSoup(page.text,'html.parser')



        for link in soup.find_all('a'):
            link_address = link.get('href')
            link_text = link.string
            Link.objects.create(address=link_address,name=link_text)
        return HttpResponseRedirect('/')
    else:
        data = Link.objects.all()


    return render(request,'myapp/result.html',{'data':data})

def clear(request):
    Link.objects.all().delete()
    return render(request,'myapp/result.html')
