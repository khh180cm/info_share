from django.db import models
from django.conf import settings


class Topic(models.Model):
    '''User can create topics'''
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )

    class Meta:
        db_table = 'topics'


class Brand(models.Model):
    kor_name      = models.CharField(max_length = 50)
    kor_letters   = models.CharField(max_length = 50)
    eng_name      = models.CharField(max_length = 50)
    sell_category = models.ManyToManyField("SellCategory", through = "BrandCategory")

    def __str__(self):
        return self.kor_name

    class Meta:
        db_table = "brands"
        verbose_name_plural = "브랜드 관리"


class BrandCategory(models.Model):
    brand    = models.ForeignKey("Brand", on_delete        = models.CASCADE)
    category = models.ForeignKey("SellCategory", on_delete = models.CASCADE)

    class Meta:
        db_table = "brands_categories"


class SellCategory(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "sell_categories"

