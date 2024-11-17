from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def submitquery(request):
    q=request.GET['query']
    try:
        ans=eval(q)
        mydictionary = {
            "q":q,
            "ans":ans,
            "error":False,
            "result":True
        }
        return render(request,'index.html',context=mydictionary)
    except Exception as e:
        mydictionary = {
            "error":True,
            "result":False
        }
        return render(request,'index.html',context=mydictionary)