from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title       = models.CharField(max_length=255)
    body        = models.TextField()
    url         = models.URLField()
    pub_date    = models.DateTimeField()
    votes_total = models.IntegerField(default=1)
    image       = models.ImageField(upload_to='images/')
    icon        = models.ImageField(upload_to='images/')
    hunter      = models.ForeignKey(User, on_delete=models.CASCADE)
        # ^ if USER is deleted, objects related to it will be deleted as well.

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, %Y')

    def summary(self):
        if len(self.body) > 150:
            return self.body[:150] + '(...)'
        else:
            return self.body

    def __str__(self):
        return (self.title)

