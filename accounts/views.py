from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

def register(req):
    if req.method == "POST":
        first_name = req.POST['first_name']
        last_name = req.POST['last_name']
        username = req.POST['username']
        email = req.POST['email']
        password = req.POST['password']
        password2 = req.POST['password2']
        
        #password check
        if password != password2:
            messages.error(req, 'Passwords do not match')
            return redirect('register')

        #username check
        if User.objects.filter(username=username).exists():
            messages.error(req, 'Username is taken')
            return redirect('register')

        #email check
        if User.objects.filter(email=email).exists():
            messages.error(req, 'Email already registered')
            return redirect('register')

        #create user
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
        user.save()
        messages.success(req, 'Succesfully created account')
        return redirect('login')
        
    else:
        return render(req, 'accounts/register.html')

def login(req):
    if req.method == "POST":
        username = req.POST['username']
        password = req.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is None:
            messages.error(req, 'Invalid credentials')
            return redirect('login')
        auth.login(req, user)
        messages.success(req, 'You are logged in')
        return redirect('dashboard')
    else:
        return render(req, 'accounts/login.html')

def logout(req):
    if req.method == 'POST':
        auth.logout(req)
        messages.success(req, 'Successfully Logged Out')
        return redirect('index')

def dashboard(req):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id = req.user.id)

    context = {
        'contacts': user_contacts
    }
    return render(req, 'accounts/dashboard.html', context)