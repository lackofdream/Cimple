from django.shortcuts import render, get_object_or_404
from .models import Code
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime


def index(request):
    try:
        title = request.POST['title']
        code = request.POST['code']
    except KeyError:
        return render(request, 'post_code/index.html')
    if len(title.strip()) == 0 or len(code.strip()) == 0:
        return render(request, 'post_code/index.html', {
            'code_title': title,
            'code_text': code,
            'error_message': 'WTF?',
        })
    new_code = Code(title=title, code_text=code, pub_date=datetime.now())
    new_code.save()
    return HttpResponseRedirect(reverse('code:code', args=(new_code.pk,)))


def view_code(request, code_id):
    code = get_object_or_404(Code, pk=code_id)
    return render(request, 'post_code/code.html', {'code': code})
