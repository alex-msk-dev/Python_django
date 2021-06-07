from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from tinyurl.models import ShortUrlModel
from .forms import RegistrationForm
from django.contrib.auth import login


def sign_up(request):
    context = {}
    form = RegistrationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    context['form'] = form
    return render(request, 'registration/sign_up.html', context)


@login_required
def lk(request):
    urls = ShortUrlModel.objects.filter(user=request.user)
    context = {
        'user': request.user,
        'urls': urls,
    }
    return render(request, 'lk.html', context)
