from django.db import models
from common.models import Lang

FEMALE = 1
MALE = 2

GENDER_CHOICES = (
    (FEMALE, "Female"),
    (MALE, "Male")
)


class Person(models.Model):
    """
    `Person` represents a person that work in the cinema world could be
    an actor, producer, director ...

    Attributes:
    """
    name = models.CharField(max_length=100)
    birthday = models.DateField(null=True, blank=True)
    death = models.DateField(null=True, blank=True)
    gender = models.IntegerField(choices=GENDER_CHOICES, null=True, blank=True)
    place_of_birthday = models.CharField(max_length=100, null=True, blank=True)
    image = models.URLField(null=True, blank=True)
    homepage = models.URLField(null=True, blank=True)
    langs = models.ManyToManyField(Lang, through='Person_lang', blank=True)

    def __str__(self):
        return self.name


class Person_lang(models.Model):
    """
    `Person_lan` is a extension to Person for language translation.

    Attributes:
    """
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    lang = models.ForeignKey(Lang, on_delete=models.CASCADE)
    biography = models.TextField()
    

class Job (models.Model):
    """
    `Job` presents diferents movie jobs.
    Attributes:
    """
    langs = models.ManyToManyField(Lang, through='Job_lang')


class Job_lang(models.Model):
    """
    `Job_lang` is a extension to Jon where translate some params.
    Attributes:
    """
    job = models.name = models.ForeignKey(Job, on_delete=models.CASCADE)
    lang = models.ForeignKey(Lang, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
