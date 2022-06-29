from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import *
from django.contrib import messages


def index(request):
    return HttpResponse('product')


def addcomment(request ,id):
    url = request.META.get('HTTP_REFERER')
    # return HttpResponse(url)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.product_id = id
            current_user = request.user
            data.user_id = current_user.id
            data.save()
            messages.success(request, "Your review has been sent.")
            return HttpResponseRedirect(url)

    return HttpResponseRedirect(url)
