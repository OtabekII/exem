from django.shortcuts import render
from .models import Kompany, Ourservis, Ourplans, Ourteem, Aboutus, Contact

def contact(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        Contact.objects.create(full_name=name, email=email, messege=message)
    return render(request, 'index.html')

def service(request):
    services = Ourservis.objects.all()
    plans = Ourplans.objects.all()
    about = Aboutus.objects.all()
    teem = Ourteem.objects.all()    

    context = {
       'services': services,
        'plans': plans,
        'about': about,
        'teem': teem
    }
    return render(request, 'index.html', context)




def index(request):
    services = Ourservis.objects.all()
    plans = Ourplans.objects.all()
    about = Aboutus.objects.all()
    teem = Ourteem.objects.all()

    context = {
       'services': services,
        'plans': plans,
        'abouts': about,
        'teems': teem
        }
    return render(request,"index.html", context=context)





def register(request):
    if request.method == 'POST':
        print(request.POST['username'])
        print(request.POST['password'])
    return render(request, 'register.html')
