from django.db import models

class  Url(models.Model):
    replace_str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' 
    replace_size = 62

    origin_url = models.CharField(max_length=3000)
    shortened_url = models.CharField(max_length=10)
    count = models.PositiveIntegerField()

    @classmethod
    def create(cls, origin_url):
        entry = cls(origin_url=origin_url, shortened_url='', count=0)
        entry.save()

        shortened_url = ''
        _id = entry.id

        while(_id > 0):
            shortened_url += cls.replace_str[_id % cls.replace_size]
            _id = _id // cls.replace_size 
        
        entry.shortened_url = shortened_url
        entry.save()

        return entry  
