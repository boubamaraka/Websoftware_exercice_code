from django.db import models


class Continent(models.Model):
    """ Write your answer in 7.1 here. """
    name=models.CharField(unique=True,max_length=100)
    code=models.CharField(unique=True,max_length=20)
    #countries=models.CharField("continent")
    class Meta:
        ordering = ["name"]


class Country(models.Model):
    """ Write your answer in 7.1 here. """
    name=models.CharField(unique=True,max_length=100)
    capital=models.CharField(max_length=100)
    code=models.CharField(unique=True,max_length=20)
    population=models.PositiveIntegerField()
    area=models.PositiveIntegerField()
    continent=models.ForeignKey(Continent,related_name="countries")
    class Meta:
        ordering = ["name"]
        #countries=['name']
