from django.urls import path
from .views import UserRegistration, UserListView, LoginView, LogoutView

urlpatterns = [
    path('register/', UserRegistration.as_view()),
    path('list-users/', UserListView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view())
]
