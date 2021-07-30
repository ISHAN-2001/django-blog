from django.db import models

# Create your models here.
class Blogs(models.Model):
    sno = models.AutoField(primary_key=True)
    category = models.CharField(max_length=20)
    topic = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    date = models.DateField(blank=True)
    desc = models.TextField()

    def __str__(self):
        return self.topic + " by " + self.author
