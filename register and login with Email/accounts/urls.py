from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'), 
    path('signup', views.sign_up, name='signup'),
    path('login',views.UserLoginView.as_view(), name='login'),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout')
]
