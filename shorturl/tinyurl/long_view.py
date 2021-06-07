from django.http import HttpRequest, HttpResponseRedirect, HttpResponseNotFound
from .storage import shorts

# Create your views here.

def full_url(request: HttpRequest, key):
    user = request.user if request.user.is_authenticated else None
    try:
        url = shorts[(key, user)]
        shorts.update_click_counter(key)
        if url.startswith('http'):
            return HttpResponseRedirect(url)
        return HttpResponseRedirect(f'http://{url}')
    except KeyError:
        return HttpResponseNotFound()
