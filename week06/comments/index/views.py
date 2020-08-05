from django.shortcuts import render
from django.http import HttpResponse
import json
# from Documents.models import Documents
from .models import Documents

from django.core import serializers
# Create your views here.


def index(request):
    comments_list = list()
    info = Documents.objects.filter(star__gt=3)[:100]
    print(info)
    for p in info:
        comments_list.append({'content': p.content, 'star': p.star, 'group_id': p.group_id, 'date_added': p.date_added})

    print(comments_list)
    # # [comments_list.append({k: v}) for k, v in info]
    # data = serializers.serialize("json", comments_list)
    # data = json.loads(data)
    # print(data)
    return render(request, 'index.html', {'results': comments_list})
