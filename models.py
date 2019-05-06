from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=160)
    content = models.TextField()
    pub_date = models.DateTimeField('publish date')
    slug = models.SlugField(max_length=30)

    def __str__(self):
        return self.title

def make_slug(self):
    """Returns a slug as a string generated from Post title"""
    temp = self.title.replace(" ", "-")

    if (len(temp) > 50):
        return temp.lower()[:51]
    else:
        return temp

def __str__(self):
    return self.title
