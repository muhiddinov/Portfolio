from django.shortcuts import render
from .models import Contact

def index_view (request):
    if (request.method == "POST"):
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        service1 = request.POST.get('electronics')
        service2 = request.POST.get('iot')
        service3 = request.POST.get('robot')
        service4 = request.POST.get('drone')
        service5 = request.POST.get('desktop')
        contact.name = name
        contact.email = email
        contact.message = message
        contact.service1 = service1
        contact.service2 = service2
        contact.service3 = service3
        contact.service4 = service4
        contact.service5 = service5
        contact.save()
    return render(request, 'index.html')