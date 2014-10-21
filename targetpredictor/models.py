from django.db import models
from django.contrib import admin


# Create your models here.
class mirna(models.Model):
    name = models.CharField(max_length=30)
    seq = models.CharField(max_length=50)
    #age  = models.IntegerField()


class mirnaAdmin(admin.ModelAdmin):
    list_display = ["name", "seq"]
    search_fields = ["name"]

