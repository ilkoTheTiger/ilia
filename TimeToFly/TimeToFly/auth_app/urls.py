from django.urls import path
from TimeToFly.auth_app.views import UserRegistrationView, UserLoginView, UserLogoutView, EditProfileView, ShowProfileView, DeleteProfileView

urlpatterns = (
    path('register/', UserRegistrationView.as_view(), name='register user'),
    path('login/', UserLoginView.as_view(), name='login user'),
    path('logout/', UserLogoutView.as_view(), name='logout user'),
    path('profile/<int:pk>/', ShowProfileView.as_view(), name='show profile'),
    path('profile/edit/<int:pk>/', EditProfileView.as_view(), name='edit profile'),
    path('profile/delete/<int:pk>/', DeleteProfileView.as_view(), name='delete profile'),
)
