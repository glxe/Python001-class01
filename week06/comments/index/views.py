from django.shortcuts import render
from django.http import HttpResponse

# from Documents.models import Documents

# Create your views here.

def index(request, **args):
    # info = Documents(group_id = 151)
    # print(info.objects)
    return HttpResponse('Hello Django!')
