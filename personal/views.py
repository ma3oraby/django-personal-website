from django.shortcuts import render
from .models import About , Experience , Services , Projects , Reviews , Faq

# Create your views here.
def home (request): 
    about = About.objects.first()
    experience_first = Experience.objects.all()[0:2]
    experience_last = Experience.objects.all()[2:]
    services = Services.objects.all()
    projects = Projects.objects.all()
    reviews = Reviews.objects.all()
    faq = Faq.objects.all()
    return render(request,'home/home.html',{
        'about':about ,
        'experience_first':experience_first ,
        'experience_last':experience_last ,
        'services':services ,
        'projects':projects , 
        'reviews':reviews , 
        'faq':faq
    })


