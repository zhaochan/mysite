from django.shortcuts import render
from django.http import HttpResponse
import json
from myapp.models import Grade
 
def Index(request):
    return render(request, 'index.html')
def welcome(request):
    return HttpResponse('welcome to Django')
def getJson(request):
    resp = {'errorcode': 100, 'detail': 'Get success'}
    return HttpResponse(json.dumps(resp), content_type="application/json")
def getGrades(request):
    # 获取所有班级
    grades = Grade.objects.all()
    context = {'gradess':grades}
    return render(request,'Grades.html',context)
# Create your views here.
