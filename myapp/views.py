from django.shortcuts import render
from django.http import HttpResponse
import json
 
def Index(request):
    return render(request, 'index.html')
def welcome(request):
    return HttpResponse('welcome to Django')
def getJson(request):
    resp = {'errorcode': 100, 'detail': 'Get success'}
    return HttpResponse(json.dumps(resp), content_type="application/json")
# Create your views here.
