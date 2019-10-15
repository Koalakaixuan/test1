from django.db import models

# Create your models here.


class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=30)


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(null=False, max_length=64, unique=True)
    publisher = models.ForeignKey(to="Publisher", on_delete=models.CASCADE)


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=30, unique=True)
    book = models.ManyToManyField(to="Book")

    def __str__(self):
        return "<Author Object:{}>".format(self.name)


    





