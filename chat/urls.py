from django.urls import path, include
from chat import views as chat_views,views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
	path("", chat_views.chatPage, name="chat-page"),
	path("loginpage/", LoginView.as_view(template_name="chat/loginpage.html"), name="login-user"),
	path("logoutpage/", LogoutView.as_view(), name="logout-user"),
	path('signuppage/', views.signup, name='signuppage'),
    #path('loginpage/', views.login_user, name='login-user'),
 
]
