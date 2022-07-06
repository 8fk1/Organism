from tabnanny import verbose
from django.db import models
import os
import hashlib
from datetime import datetime

class Domain(models.Model):
    name = models.CharField('名前', max_length=16)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'domain'
        verbose_name = 'ドメイン'
        verbose_name_plural = 'ドメイン'


class Kingdom(models.Model):
    name = models.CharField('名前', max_length=16)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'kingdom'
        verbose_name = '界'
        verbose_name_plural = '界'

# ドメイン　界　門　綱　目　科　属　種


class Division(models.Model):
    name = models.CharField('名前', max_length=16)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'division'
        verbose_name = '門'
        verbose_name_plural = '門'


class Classis(models.Model):
    name = models.CharField('名前', max_length=16)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'class'
        verbose_name = '綱'
        verbose_name_plural = '綱'


class Order(models.Model):
    name = models.CharField('名前', max_length=16)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'order'
        verbose_name = '目'
        verbose_name_plural = '目'


class Family(models.Model):
    name = models.CharField('名前', max_length=16)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'family'
        verbose_name = '科'
        verbose_name_plural = '科'

def _organism_pic_upload_to(instance, filename):
    current_time = datetime.now()
    pre_hash_name = '%s%s%s' % (instance.id, filename, current_time)
    extension = str(filename).split('.')[-1]
    hs_filename='%s.%s' % (hashlib.md5(pre_hash_name.encode()).hexdigest(), extension)
    saved_path='images/'
    return '%s%s' % (saved_path, hs_filename)


class Organism(models.Model):
    """ 生物 """
    STATUS_SURVIVAL = 0
    STATUS_EXTINCT = 1

    STATUS_CHOICES = (
        (STATUS_SURVIVAL, '生存'),
        (STATUS_EXTINCT, '絶滅')
    )

    def __str__(self):
        return self.name_ja

    name_ja = models.CharField('名前', max_length=32)
    name_en = models.CharField('Name', max_length=64)
    domain = models.ForeignKey(Domain,
                               verbose_name='ドメイン',
                               on_delete=models.CASCADE,
                               related_name='organism',
                               blank=True, null=True)
    kingdom = models.ForeignKey(Kingdom,
                                verbose_name="界",
                                on_delete=models.CASCADE,
                                related_name='organism',
                                blank=True, null=True)
    division = models.ForeignKey(Division,
                                 verbose_name="門",
                                 on_delete=models.CASCADE,
                                 related_name='organism',
                                 blank=True, null=True)
    classis = models.ForeignKey(Classis,
                                verbose_name="綱",
                                on_delete=models.CASCADE,
                                related_name='organism',
                                blank=True, null=True)
    order = models.ForeignKey(Order,
                              verbose_name="目",
                              on_delete=models.CASCADE,
                              related_name='organism',
                              blank=True, null=True)
    family = models.ForeignKey(Family,
                               verbose_name='科',
                               on_delete=models.CASCADE,
                               related_name='organism',
                               blank=True, null=True)

    status = models.PositiveIntegerField(
        "生存ステータス", choices=STATUS_CHOICES, default=STATUS_SURVIVAL, blank=True)

    outline = models.TextField(verbose_name='概要', blank=True)
    picture = models.ImageField(
        verbose_name='画像',
        #upload_to='images/',
        upload_to = _organism_pic_upload_to,
        blank=True,
        null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'organism'
        verbose_name = '生物'
        verbose_name_plural = '生物'

    def isSurvival(self):
        """ 生存しているならTrueを返す
        """
        return self.status == self.STATUS_SURVIVAL

    def getNameText(self):
        name = []
        for e in self.name_en.split('_'):
            name.append(e.capitalize())
        return ' '.join(name)

    def save(self, *args, **kwargs):
        self.name_en = self.name_en.replace(' ', '_').lower()
        return super(Organism, self).save(*args, **kwargs)


class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=2, choices=SHIRT_SIZES)
