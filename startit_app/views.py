from django.shortcuts import render, get_object_or_404, redirect
from .models import Quest, addresesQ, infotxt
from django.contrib.auth import login, authenticate, logout
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
def home_page(request):
    quests = Quest.objects.all().order_by('-created_at')
    unique_ages = Quest.objects.values('age__name').distinct()
    unique_slozhno = Quest.objects.values('slozhno__name').distinct()
    unique_strashno = Quest.objects.values('strashno__name').distinct()
    infotxts = infotxt.objects.all()

    return render(request, "index.html", {
        'quests': quests,
        'unique_ages': unique_ages,
        'unique_slozhno': unique_slozhno,
        'unique_strashno': unique_strashno,
        'infotxts' : infotxts 
    })

def book_page(request, pk):
    quest = get_object_or_404(Quest, pk=pk)
    addresesq = addresesQ.objects.all()
    return render(request, "book-page.html", {
        'quest': quest,
        'addresesq': addresesq,
    })

def quests_by_home_page(request, slug):
    addresesQ = get_object_or_404(addresesQ, slug=slug)
    quests = Quest.objects.filter(addresesQ=addresesQ)
    context = {
        'addresesQ': addresesQ,
        'quests': quests,
    }
    return render(request, "./quests_by_addresesQ.html", context)

def sign_up_page (request):
    if request.method == "POST":
        form =  NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('lodin_page')
    else:
        form =NewUserForm()
    context = {
        'form' : form
    }
    return render(request, "sign_up.html", context)

def login_page(request):
    if request.method == "POST":
            form = AuthenticationForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data('username')
                password = form.cleaned_data('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home_page')
    else:
        form = AuthenticationForm()

    context = {
        'form': form
    }
    return render(request, "login.html", context)

def logout_action(request):
    logout(request)
    return redirect('home_page')