from django.shortcuts import render, redirect

from item.models import Category,Item

from .forms import SignupForm

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    return render(request, 'core/index.html',{
        'categories':categories,
        'items':items,
    })

def contacts(request):
    return render(request, 'core/contacts.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid(): 
            form.save() # if data is valid it is saved into database
            return redirect('/login/')
    else:
        form = SignupForm()

    form = SignupForm()

    
    return render(request, 'core/signup.html', {
        'form': form
    })