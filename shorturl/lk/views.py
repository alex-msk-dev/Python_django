from django.shortcuts import render
from .forms import AuthForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth import  authenticate, login

def auth(request: HttpRequest):
    go_next = request.GET.get('redirect', '/')
    if request.user .is_authenticated:
        return HttpResponseRedirect(go_next)
    auth_form = AuthForm(request.POST)
    if not auth_form.is_valid():
        return HttpResponseBadRequest
    user = authenticate(request, auth_form.cleaned_data)
    if user:
        login(request, user)
        return HttpResponseRedirect(go_next)
    return HttpResponseNoAllowed()