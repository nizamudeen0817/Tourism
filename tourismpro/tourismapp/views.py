from django.shortcuts import render,redirect 
from .models import Tourismcard
from.forms import Bookingform
# Create your views here.
def index(request):
    tourismcard=Tourismcard.objects.all()
    context={
        'card':tourismcard
    }
    return render(request,'index.html',context)


def Booking(request):
    if request.method=='POST':
        forms= Bookingform(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/')
    forms=Bookingform()
    book={
        'form':forms
    }
    return render(request,'booking.html',book)
    
    
    
    return render(request,'index.html',context)

    
