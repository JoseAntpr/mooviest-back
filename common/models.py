from django.db import models


class Lang(models.Model):
    """
    `Lang` represents an idiom that the user can select while using the 
    application.Determines how should be translated other models like a 
    `Country`, `Movie`...

    Attributes:
    """
    code = models.CharField(max_length=20)
