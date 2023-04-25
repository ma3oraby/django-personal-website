from django.db import models

# Create your models here.

class About (models.Model) : 
    about = models.CharField(max_length=1000)
    logo = models.ImageField(upload_to='logo')
    fb_link = models.URLField(null=True,blank=True)
    iesta_link = models.URLField(null=True,blank=True)
    twitter_link = models.URLField(null=True,blank=True)
    youtube_link = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.about 


class Experience (models.Model) :
    from_to = models.CharField(max_length=20)
    title = models.CharField(max_length=35)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title

class Services (models.Model) :
    icon = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title 

class Projects (models.Model) : 
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects')
    subtitle = models.CharField(max_length=100)
    description = models.TextField(max_length=15000)

    def __str__(self):
        return self.title 

class Reviews (models.Model) : 
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='reviews')
    job_title = models.CharField(max_length=35)
    review = models.TextField(max_length=400)

    def __str__(self):
        return self.name 

class Faq (models.Model) : 
    question = models.CharField(max_length=250) 
    answer = models.CharField(max_length=450) 

    def __str__(self):
        return self.question

class Contact (models.Model) : 
    name = models.CharField(max_length=100)
    email = models.EmailField()
    details = models.TextField(max_length=1000)