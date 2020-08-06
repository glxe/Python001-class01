from django.shortcuts import render
from django.http import HttpResponse
import json
# from Documents.models import Documents
from .models import Documents

from django.core import serializers
from datetime import *
import time
# Create your views here.


def index(request):
    key = request.GET.get('key')
    print(key)
    comments_list = list()
    if key:
        info = Documents.objects.filter(content__contains = key)[:100]
    else:
        info = Documents.objects.filter()[:100]
    k = 0
    for p in info:
        comments_list.append({'key': k, 'content': p.content, 'star': p.star, 'group_id': p.group_id, 'date_added': p.date_added.strftime('%Y-%m-%d %H:%M:%S')})
        k += 1

    # # [comments_list.append({k: v}) for k, v in info]
    # data = serializers.serialize("json", comments_list)
    # data = json.loads(data)
    # print(data)
    return render(request, 'index.html', {'results': comments_list})
