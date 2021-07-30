from django.shortcuts import render , HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    # return HttpResponse("Home page")
    return render(request,'home/home.html')

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        content = request.POST['message']

        contact = Contact(name= name , email = email , phone =phone, content= content)
        contact.save()

        print(name,phone,email,content)
    return render(request, 'home/contact.html')

def about(request):
    return render(request , 'home/about.html')