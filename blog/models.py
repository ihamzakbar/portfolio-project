from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=32)
    datetime = models.DateTimeField()
    blog_body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def summary(self):
        return self.blog_body[:35]

    def datetime_pretty(self):
        return self.datetime.strftime('%b %e %Y')

    def __str__(self):
        return self.title
