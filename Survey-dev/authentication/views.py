from django.shortcuts import render
from django.contrib import auth, messages
from django.shortcuts import redirect
from django.urls.base import reverse


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect(reverse('polls:polls', args=(username, )))
        else:
            messages.info(request, 'Credentials are invalid.')
            return redirect(reverse('authentication:login'))
    else:
        return render(request, 'authentication/login.html')


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email_id = request.POST['email_id']
        password = request.POST['password']
        repeated_password = request.POST['repeated_password'] 
        if password == repeated_password:
            if auth.models.User.objects.filter(email=email_id).exists():
                messages.info(request, 'Email ID already used.')
                return redirect(reverse('authentication:register'))
            elif auth.models.User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken.')
                return redirect(reverse('authentication:register'))
            else:
                user = auth.models.User.objects.create_user(username=username, email=email_id, password=password)
                user.save()
                return redirect(reverse('authentication:login'))
        else:
            messages.info(request, 'Entered passwords must be the same.')
            return redirect('authentication:register')
    else:
        return render(request, 'authentication/register.html')

