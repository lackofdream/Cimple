from django.db import models


def pkgen():
    from base64 import b64encode
    from hashlib import md5
    from random import random
    text = b64encode(md5(str(random()).encode()).digest()).decode('ascii')
    ret = ''
    while len(ret) != 8:
        if str.isalnum(text[0]):
            ret += text[0]
        text = text[1:]
    return ret


class Code(models.Model):
    hash_key = models.CharField(max_length=8, primary_key=True, unique=True, editable=False, default=pkgen)
    title = models.CharField(max_length=100)
    code_text = models.TextField('code', max_length=1000000)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title
