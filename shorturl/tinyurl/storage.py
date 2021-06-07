from collections import UserDict
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F

from .models import ShortUrlModel

class ShortUrlsStorage(UserDict):
    def __init__(self):
        super().__init__()
        self.hash_length = 2

    def __missing__(self, key_user):
        key, user = key_user
        try:
            self.short_url_db = short_url_db = ShortUrlModel.objects.get(hash=key, user=user)
        except ObjectDoesNotExist:
            raise KeyError()
        self[short_url_db.hash] = short_url_db.url
        return short_url_db.url

    def to_key(self, url, user=None):
        url_hash = hash(url)
        while True:
            short_hash = url_hash % self.hash_length
            key = f'{short_hash:x}'
            saved_url = self.get((key, user), None)
            if saved_url is None:
                self._save(key, url, user)
                return key
            if saved_url == url:
                return key
            self.hash_length += 1

    def _save(self, key, url, user=None):
        self[key] = url
        short_url_db = ShortUrlModel()
        short_url_db.hash = key
        short_url_db.url = url
        short_url_db.user = user
        short_url_db.save()

    def update_click_counter(self, key):
        ShortUrlModel.objects.filter(hash=key).update(click_counter=F('click_counter') + 1)

shorts = ShortUrlsStorage()
