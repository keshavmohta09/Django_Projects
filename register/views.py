from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.models import User , auth


def index_google(request):
    return render(request, 'index_google.html')
    auth.index_google(request)
    return redirect('/')

def login_fb(request):
    return render(request, 'login_fb.html')


def home_fb(request):
    return render(request, 'home_fb.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    return render(request, 'login.html')

def register1(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        con_password = request.POST['con_password']
        email = request.POST['email']


        if password==con_password:
            if User.objects.filter(username=username).exists():

                messages.info(request,'username taken')
                #return redirect('register1');

            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                #return redirect('register1');
            else:
                user = User.objects.create_user(username=username, password=password, email=email,
                                                first_name=first_name,
                                                last_name=last_name)
                user.save();
                return render(request,'login.html')
            
    else :
        return render(request, 'register.html')
    
    
def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/index')
        else:
            messages.info(request, 'invalid usename or password')
            return redirect('login')

    else:
        return render(request, 'login.html')






