from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=32)
    datetime = models.DateTimeField(auto_now=True)
    blog_body = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/')
# Create a Blog model
# Title
# pub_date
# body
# image



# add the blog app to settings
# create migration
# migrate
# add to admin

