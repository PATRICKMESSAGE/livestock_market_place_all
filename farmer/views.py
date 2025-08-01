from django.shortcuts import render, redirect

from item.models import Item, Category

from .forms import SignupForm

def index(request):
    items = Item.objects.filter(is_sold=False) [0:10]
    categories = Category.objects.all()
    
    return render(request, 'farmer/index.html', {
        'categories': categories,
        'items': items,
    })
    
def contact(request):
    return render(request, 'farmer/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('/login/') 
    else:
      form = SignupForm()
    
    return render(request, 'farmer/signup.html', {
        'form': form,
    })