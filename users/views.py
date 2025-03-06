from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, UpdateView
from .models import CustomUser
from .forms import UserSignUpForm, UserSignInForm, UserUpdateForm
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.

class SignUpView(CreateView):
    model = CustomUser
    form_class = UserSignUpForm
    template_name = 'main/auth/sign_up.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class SignInView(LoginView):
    form_class = UserSignInForm
    template_name = 'main/auth/sign_in.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

def user_logout(request):
    logout(request)
    return redirect('login')


class ProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'main/profile.html'
    context_object_name = 'user_profile'

    def get_object(self, queryset=None):
        return self.request.user


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = UserUpdateForm
    template_name = 'main/profile_edit.html'
    context_object_name = 'user_profile'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user

class UserPasswordChangeView(PasswordChangeView):
    template_name = 'main/change-password.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, '✅ Your password has been changed successfully')
        return super().form_valid(form)