
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth



# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"login invalid")
            return redirect('login')

    return render(request,'login.html')



def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirmpass = request.POST['confirmpass']
        if password==confirmpass:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,email=email,last_name=lastname,first_name=firstname)
                user.save();
                return redirect('login')

        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
# Create your views here.
def form(request):
    # if request.method == 'POST':
     return  render(request,'form.html')
        # name = request.POST['name']
        # date = request.POST['date']
        # age = request.POST['age']
        # pnumber = request.POST['pnumber']
        # email = request.POST['email']
        # address = request.POST['address']
        # address = request.POST['category']
        # address = request.POST['items']
        # address = request.POST['accounttype']
        # user = User.objects.create_user(username=username, password=password, email=email, last_name=lastname,
        #                                 first_name=firstname)
        # if name is not  :
        #     return render(request, 'aceepted.html')
        # else:
        #     messages.info(request,"no name")
        #     return redirect('form')


        # if request.POST['name'] :
        #    news.name = request.POST['name']
        #
        # else:
        #     print('No name submitted')




    # return render(request,"form.html")
def aceepted(request):

    return render(request,'aceepted.html')
