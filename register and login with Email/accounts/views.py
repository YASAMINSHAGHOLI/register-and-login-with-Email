from django.shortcuts import render  , redirect
from django.views import View 
from .forms import LoginForm ,UserCreationForm
from django.contrib.auth import authenticate , login
from django.contrib.auth.views import LogoutView

def home (request):
    return render(request, 'accounts/home.html')

  
def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            fullname = form.cleaned_data.get('fullname')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password,fullname=fullname)
            login(request,user)
            return redirect('home')
    else:
        form = UserCreationForm()  
    return render(request, 'accounts/register.html',{'form':form})


class UserLoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'accounts/login.html' , {'form': form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error("Invalid email or password")
        else:
            form.add_error("email","Invalid data ")
        
        return render(request, 'accounts/login.html' , {'form': form})    
            
            
            
        
class LogoutInterfaceView(LogoutView):
    template_name = 'accounts/home.html'

