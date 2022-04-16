from django.contrib.auth import views as auth_views
from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth import forms as auth_forms, get_user_model
from django.views import generic as views
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login, logout
from TimeToFly.auth_app.models import Profile
from django import forms

UserModel = get_user_model()

class UserRegistrationForm(auth_forms.UserCreationForm):

    IMAGE_UPLOAD_DIR = 'images/'
    MAX_FILE_SIZE_IN_MEGABYTES=1

    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)

    class Meta:
        model = UserModel
        fields = ('email', )

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(first_name=self.cleaned_data['first_name'],
                          last_name=self.cleaned_data['last_name'],
                          user=user,
                          )
        if commit:
            profile.save()

        return user


class UserRegistrationView(views.CreateView):
    form_class = UserRegistrationForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('show index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result

class UserLoginView(auth_views.LoginView):
    template_name = 'auth/login.html'

    def get_success_url(self):
        return reverse_lazy('show index')

class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('show index')


class ShowProfileView(auth_mixins.LoginRequiredMixin, views.DetailView):
    model = Profile
    template_name = 'auth/show-profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.object.user == self.request.user

        return context

class EditProfileView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = Profile
    fields = ('first_name', 'last_name', 'age', 'passport', 'image')
    # success_url = reverse('show profile')
    template_name = 'auth/edit-profile.html'

    def get_success_url(self):
        return reverse('show profile', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.object.user == self.request.user

        return context

class DeleteProfileView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = Profile
    template_name = 'auth/delete-profile.html'
    success_url = reverse_lazy('show index')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.object.user == self.request.user

        return context

    def form_valid(self, form):
        result = super().form_valid(form)
        logout(self.request)
        return result
