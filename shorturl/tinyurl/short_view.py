from django.http import HttpRequest, HttpResponseNotAllowed, HttpResponseBadRequest
from django.shortcuts import render
from .full_url_form import FullUrlFrom
from .storage import shorts

# Create your views here.
def short_url(request: HttpRequest):
    if request.method !='POST':
        return HttpResponseNotAllowed(['POST'])
    url_form = FullUrlFrom(request.POST)
    if not url_form.is_valid():
        return HttpResponseBadRequest()
    url = url_form.cleaned_data['url']
    user = request.user if request.user.is_authenticated else None
    key = shorts.to_key(url, user)
    host = request.get_host()
    schema = request.scheme

    url = f'{schema}://{host}/s/{key}'
    return render(request, 'short.html', {'url': url})
